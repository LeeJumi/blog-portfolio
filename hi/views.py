from django.shortcuts import render
from .models import hi 

# Create your views here.
def home(request):
    his = Hi.objects
    return render(request, 'hi/home.html',{'his':his})
    
def detail(request, hi_id):    
    hi_detail = get_object_or_404(hi, pk = hi_id)
    return render(request, 'detail.html',{'hi':hi_detail})

def new(request):
    return reder(request, 'new.html')

def create(request):
    hi = Hi()
    hi.title = request. GET['title']
    hi.body = request. GET ['body']
    hi.pub_date = timezone.datetime.now()
    hi.save()
    return redirect('/hi/'+str(hi.id))