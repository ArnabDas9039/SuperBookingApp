from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def get_by_query(request):
    category = request.GET.get("category") #it's a category name not id
    name = request.GET.get("name")
    location = request.GET.get("location")
    latitude = request.GET.get("latitude")
    longitude = request.GET.get("longitude")
    entry_fee_base = request.GET.get("entry_fee")
    is_open = request.GET.get("is_open")
    opening_time = request.GET.get("opening_time")
    closing_time = request.GET.get("closing_time")
    







