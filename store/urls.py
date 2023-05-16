from django.urls import path
from . import views



urlpatterns = [
    path('search/',views.search, name='search'),
    path('cart/',views.cart_view, name='cart_view'),
    path('remove-from-cart/<int:book_id>/',views.removeFromCart,name = 'removeFromCart'), 
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'), 
    path('checkout/',views.checkout, name='checkout'),
    path('reservation-receipt/',views.reservation_receipt, name='reservation_receipt'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
   
    path('<slug:slug>/',views.book_detail, name='book_detail'),
   
]