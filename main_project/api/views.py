from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import F
from rest_framework.response import Response
from .models import *
from django.contrib.contenttypes.models import ContentType
from .serializer import *

class InvoiceView(APIView):
    def post(self, request):
        try:
            serializer = InvoiceWriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': "Invoice created successfully", 'status': 200}, status=200)
            else:
                return Response({'data': serializer.errors, 'message': 'Something went wrong', 'status': 400}, status=400)
        except Exception as err:
            return Response({'data': str(err), 'message': 'Something went wrong', 'status': 400}, status=400)
    def put(self, request):
        try:
            invoice = InvoiceModel.objects.filter(invoice_number=request.data["invoice_number"])
            serializer = InvoiceWriteSerializer(invoice.first(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': "Invoice details updated successfully", 'status': 200}, status=200)
            else:
                return Response({'data': serializer.errors, 'message': 'Something went wrong', 'status': 400}, status=400)
        except Exception as err:
            return Response({'data': str(err), 'message': 'Something went wrong', 'status': 400}, status=400)
