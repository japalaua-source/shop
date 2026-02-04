from django.shortcuts import render
def catalog(request):
    return render(request, 'shop/catalog.html')
# Create your views here.
