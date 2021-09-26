from account.models import Account
from django.shortcuts import render
import random

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.serializers import SignupSerializer
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def signup_view(request):

    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user."
            data['mobile_num'] = account.mobile_num
            # headers = request.get_success_headers(serializer.data)
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

"""

Tried working on OTP method but it took almost hours but still haven't find a way to do it.

That's why did it with--
    Mobile number as USERNAME
    assword as PASSWORD

"""
# def send_otp(phone):
#     if phone:
#         key = random.randint(999,9999)
#         print(key)
#         return key
#     else:
#         return False


# @api_view(['POST'])
# def signup_view(request):

#     if request.method == 'POST':
#         serializer = SignupSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             phone_number = request.data.get('mobile_num')
#             phone  = str(phone_number)
#             user = Account.objects.filter(mobile_num__iexact = phone)
#             if user.exists():
#                 key = send_otp(phone)
#                 user.set_password(key)
#                 Account.objects.filter(mobile_num__iexact = phone).update(password=key)
#                 data['otp'] = key
#                 data['response'] = "successfully sent the otp to user."
#             else:
#                 account = serializer.save()
#                 key = send_otp(phone)
#                 Account.objects.filter(mobile_num__iexact = phone).update(otp=key)
#                 data['key'] = key
#                 data['response'] = "successfully registered a new user."
#                 # token = Token.objects.create(user=account)
#                 # data['token'] = token
#         else:
#             data = serializer.errors
#         return Response(data)


# @api_view(['POST'])
# def validation_view(request):
    
#     if request.method == 'POST':
#         serializer = ValidationSerializer(data=request.data)
#         if serializer.is_valid():
#             phone = request.data.get('mobile_num')
#             otp_sent = request.data.get('otp')

#             user = Account.objects.filter(mobile_num__iexact = phone)
#             if user.exists():
#                 # user = user.first()
#                 otp = user.otp
#                 if str(otp_sent) == str(otp):
#                     user.validated = True
#                     user.save()
#                     return Response({
#                         'status' : True,
#                         'detail' : 'OTP matched. Please proceed to use.'
#                         })
#                 else: 
#                     return Response({
#                         'status' : False,
#                         'detail' : 'OTP incorrect.'
#                         })
#             else:
#                 return Response({
#                     'status' : False,
#                     'detail' : 'First proceed via sending otp request.'
#                     })
#         else:
#             return Response({
#                 'status' : False,
#                 'detail' : 'Please provide both phone and otp for validations'
#                 })