from django.shortcuts import render ,get_object_or_404, redirect
from django.db.models import Q
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
import datetime
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .cart import Cart
from .models import Book, OrderItem, Order

def search(request):
    query=request.GET.get('query', '')
    books=Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request,'store/search.html',{'query':query,'books':books})

    
def book_detail(request,slug):
    
    booky=get_object_or_404(Book,slug=slug)
    return render(request, 'store/book_detail.html',{'book':booky })

def cart_view(request):
    cart = Cart(request)
    return render(request, 'store/cart_view.html', {'cart':cart})


def add_to_cart(request, book_id):

        if request.method == 'POST':
            rental_duration = int(request.POST.get('rental_duration'))
            

        cart = Cart(request)
        cart.add(book_id,rental_duration)

        return redirect('cart_view')

def removeFromCart(request,book_id):
     cart = Cart(request)
     cart.remove(book_id)
     return redirect('cart_view')

data = {}
list_copies = []
list_prices = []
list_due_date = []

@login_required
def checkout(request):
    cart = Cart(request)
     
    if request.method == 'POST' :
            form = OrderForm(request.POST)
            if form.is_valid():
               total_price = 0
               for item in cart :
                    book = item['book']
                    total_price += book.price * int(item['rental_duration'])
               order = form.save(commit=False)
               order.created_by = request.user
               order.paid_amount = total_price
               order.save()
               data['id']= order.id
               data['creation_date'] = order.created_at
               data['first_name'] =order.first_name
               data['last_name'] = order.last_name
               data['address'] = order.address
               data['city'] = order.city
               
              
               

               for item in cart :
                    book = item['book']
                    book.available_copies -= 1
                    book.save()
                    copies = book.copies.filter(reserved=False)
                    copies_list = list(copies)
                    copy = copies_list[0]
                    copy.reserved = True
                    copy.due_date = item['due_date']
                    list_due_date.append(copy.due_date)
                    copy.save()
                    list_copies.append(copy)
                    
                    rental_duration = int(item['rental_duration'])
                    price = book.price * rental_duration
                    list_prices.append(price)
                    data['books_prices_due_date'] = zip(list_copies,  list_prices, list_due_date )
                    data['total_price'] = sum(list_prices)
                    item = OrderItem.objects.create(order=order, book=book, price = price, rental_duration=rental_duration)
               
               cart.clear()
               
               return redirect('reservation_receipt')
    else:
        form = OrderForm() 
    return render(request,'store/checkout.html',{'cart':cart, 'form': form})


def reservation_receipt(request):
    return render(request, 'store/reservation_receipt.html')





def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None







class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('store/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('store/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response


