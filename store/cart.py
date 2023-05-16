from django.conf import settings
from store.models import Book
import datetime

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart


    def __iter__(self):
        today = datetime.datetime.today().date()
            
        for p in self.cart.keys():
            self.cart[str(p)]['book'] = Book.objects.get(pk=p)
        
        for item in self.cart.values():
            item['total_price'] = int(item['book'].price * item['rental_duration'])
           
            item['due_date'] = today + datetime.timedelta(days=item['rental_duration'])


            yield item

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True



    def add(self, book_id, rental_duration):
       
       
        
        book_id = str(book_id)

        
        if book_id not in self.cart and rental_duration >= 1:
            self.cart[book_id] = {'rental_duration': rental_duration, 'id': book_id}
        
        
            
        self.save()  



    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['book'] = Book.objects.get(pk=p)

        return int(sum(item['book'].price * item['rental_duration'] for item in self.cart.values()))


    def remove(self,book_id ):
        if str(book_id) in self.cart:
            del self.cart[str(book_id)] 
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def __len__(self):
        return len(self.cart.keys())