from django.shortcuts import render, HttpResponse

# Create your views here.

# pages in this app:
# Home
# About us
# Contact Us
# Members
# Hiring Project Manager (Important)

def index(request):
    return HttpResponse('webyo')
