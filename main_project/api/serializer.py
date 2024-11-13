from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *
from datetime import datetime


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetailsModel
        fields = ['id', 'quantity', 'price', 'description', 'line_total']
    def validate(self, attrs):
        if attrs["quantity"] * attrs["price"] != attrs["line_total"]:
            raise ValidationError("Incorrect calculations")
        if len(attrs["description"]) < 3:
            raise ValidationError("Description should contain more than 2 characters.")
        return attrs

class InvoiceWriteSerializer(serializers.ModelSerializer):
    details = InvoiceDetailsSerializer(many=True)
    class Meta:
        model = InvoiceModel
        fields = ['id', 'invoice_number', 'date', 'customer_name', 'details']

    def validate(self, attrs):
        if not attrs.get("customer_name"):
            raise ValidationError("Customer name is required.")
        if not attrs.get("date"):
            raise ValidationError("Date is required.")
        if len(attrs["customer_name"]) < 3:
            raise ValidationError("Customer name should contain atleast two characters.")     
        if attrs["date"] < datetime.now().date():
            raise ValidationError("Date should be greater than or equal to today's date.")
        return attrs

    def create(self, validated_data):
        invoice_details = validated_data.pop("details")
        invoice = InvoiceModel.objects.create(**validated_data)
        invoice_details_objects = []
        for inv_details in invoice_details:
            invoice_details_objects.append(InvoiceDetailsModel(invoice=invoice, **inv_details))
        InvoiceDetailsModel.objects.bulk_create(invoice_details_objects)
        return invoice

    def update(self, instance, validated_data):
        invoice_details = validated_data.pop("details")
        instance.customer_name = validated_data["customer_name"]
        instance.date = validated_data["date"]
        instance.details.all().delete()
        invoice_details_objects = []
        for inv_details in invoice_details:
            invoice_details_objects.append(InvoiceDetailsModel(invoice=instance, **inv_details))
        InvoiceDetailsModel.objects.bulk_create(invoice_details_objects)
        return instance
