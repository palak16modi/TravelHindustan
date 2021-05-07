from django.shortcuts import render

# Create your views here.
def Contact_us(request):
    return render(request,"contact_us/contact_us.html")