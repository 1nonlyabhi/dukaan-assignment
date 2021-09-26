from django.shortcuts import render
from django.db.models import Count
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from store.models import Category, Product, Store
from django.utils.text import slugify
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from store.serializers import ProductSerializer, StoreSerializer

# Create your views here.
class StoreView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        store = Store.objects.filter(owner = self.request.user)
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data)
  
    # POST request for creating new alert/targetPrice
    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            store = serializer.save(owner=self.request.user)
            data['response'] = "successfully created a new store."
            data['store_name'] = store.store_name
            data['address'] = store.address
            data['store_link'] = "localhost:8000/api/store/{}".format(store.slug)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        store = Store.objects.get(id = request.data['id'])
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH request to edit partial data { In this you can flag to an item }
    def patch(self, request, format=None):
        store = Store.objects.get(id = request.data['id'])
        serializer = StoreSerializer(store, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # this DELETE request will delete the data from database
    def delete(self, request, format=None):
        if self.request.user.is_authenticated:
            store = Store.objects.get(id = request.data['id'])
            store.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def detail_store_view(request, slug):

    try:
        store = Store.objects.get(slug=slug)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        store_serializer = StoreSerializer(store)
        product = Product.objects.filter(store=store)
        product_serializer = ProductSerializer(product, many=True)
        return Response({
            'store_detail': store_serializer.data,
            'product_detail': product_serializer.data
        })


class ProductView(APIView):
    permission_classes = [IsAuthenticated]
  
    # POST request for creating new alert/targetPrice
    def post(self, request, slug, format=None):
        serializer = ProductSerializer(data=request.data)
        try:
            store = Store.objects.get(slug=slug)
            print(store)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if store.owner != self.request.user:
            return Response({'response': "You don't have the permission to add this product in other's store."})

        if serializer.is_valid():
            category = request.data.get('category')
            categ = Category.objects.filter(title__iexact=category).first()
            if categ is None:
                categ = Category.objects.create(title=category)
            serializer.save(category=categ, store=store)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug, format=None):
        try:
            store = Store.objects.get(slug=slug)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product = Product.objects.get(id = request.data['id'])

        if product.store.owner != self.request.user:
            return Response({'response': "You don't have the permission to edit this product."})
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            category = request.data.get('category')
            categ = Category.objects.filter(title__iexact=category).first()
            if categ is None:
                categ = Category.objects.create(title=category)
            serializer.save(category=categ, store=store)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # this DELETE request will delete the data from database
    def delete(self, request, slug, format=None):
        if self.request.user.is_authenticated:
            try:
                store = Store.objects.get(slug=slug)
                product = Product.objects.get(id = request.data['id'])
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if product.store.owner != self.request.user:
                return Response({'response': "You don't have the permission to delete this product."})
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


"""
Tried this one but still didn't get through this... -->>
"""


@api_view(['GET'])
def detail_store_cat_view(request, slug):

    try:
        store = Store.objects.get(slug=slug)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = []
        product2 = Product.objects.filter(store=store).values('category').annotate(total=Count('id')).order_by('total')
        # for dic in product2:
        #     for key in dic:
        #         if key == "category":
        #             print(dic[key])
        #             product = Product.objects.filter(store=store)
        #             product_serializer = ProductSerializer(product, many=True)
        #             data.append(product_serializer.data)
        product = Product.objects.filter(store=store)
        product_serializer = ProductSerializer(product, many=True)
        return Response(product_serializer.data)