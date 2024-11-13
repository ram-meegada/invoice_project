from django.urls import path
from .views import *

urlpatterns = [
    path('api/invoices/', InvoiceView.as_view(), name='invoice')
]
