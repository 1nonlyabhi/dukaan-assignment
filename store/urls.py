from django.urls import path
from account.views import *

from store.views import ProductView, StoreView, detail_store_cat_view, detail_store_view

app_name = "store"


urlpatterns = [
    path('', StoreView.as_view(), name="store"),
    path('<slug>/', detail_store_view, name="detail"),
    path('<slug>/product', ProductView.as_view(), name="product"),
    path('<slug>/category', detail_store_cat_view, name="category"),
]