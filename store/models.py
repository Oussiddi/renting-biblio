from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from UserProfile.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid





class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    slug =models.SlugField(default='', null='false')
    description = models.TextField(blank=True,null=True)
    year_published = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/book_images/')
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('off loan', 'Off loan')])

    

    def __str__(self):
        return self.title
    
    
    
    def save(self, *args, **kwargs):
        # Si le nombre d'exemplaires disponibles est égal à 1, définir le champ "status" sur "hors-pret"
        if self.available_copies <= 1:
            self.status = 'off loan'
        else :
            self.status = 'available'

    

        super().save(*args, **kwargs)

  




class BookCopy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=12, unique=True,null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    reserved = models.BooleanField(default=False)
    rented = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    lost = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    lost_date = models.DateField(null=True, blank=True)
    damaged = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    removed_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def mark_lost(self):
       
        self.lost = True
        self.lost_date = date.today()
        self.save()

    def mark_returned(self):
       
        self.reserved = False
        self.rented = False
        self.return_date = date.today()
        self.save()
        if self.lost and (date.today() - self.lost_date) > timedelta(days=365):
            self.delete()

    def generate_uuid():
        return uuid.uuid4()

    def save(self, *args, **kwargs):
        if self.is_paid :
            self.rented = True
        else :
            self.rented = False

    

        super().save(*args, **kwargs)


    

    def __str__(self):
        return f"{self.book.title} ({self.id})"

@receiver(post_save, sender=Book)
def create_copies(sender, instance, created, **kwargs):
    if created:
        for i in range(instance.total_copies):
            BookCopy.objects.create(book=instance)








class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    rental_duration = models.IntegerField(default=0)