from django.shortcuts import render
from ..posts.models import Post

# Create your views here.

def index(request):

    return render(request,'index.html')
