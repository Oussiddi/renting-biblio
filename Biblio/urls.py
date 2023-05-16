
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from core.views import frontpage, about, contact, List_Books, rent, privacy,consultation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',List_Books, name='books'),
    
    path('',frontpage, name ='frontpage'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    
    path('rent/',rent, name='rent'),
    path('privacy/',privacy, name='privacy'),
    path('consultation/',consultation, name='consultation'),
    path('',include('UserProfile.urls')),
    path('', include('store.urls')), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
