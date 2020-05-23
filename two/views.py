from django.shortcuts import render
from .models import two

# Create your views here.
def two(request):
    two = two.objects
    return render(request, 'portfolio.html', {'twos':portfolios})
    