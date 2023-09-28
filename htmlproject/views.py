from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import render
from htmlapp.models import Students,FilesUpload
from htmlapp.resources import StudentsResource
from django.contrib import messages
from django.db.models import Q
from tablib import Dataset
from htmlproject.forms.forms import SearchForm
# Create your views here.
def home(request):
    POST=Students.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        POST=Students.objects.filter(Q(S_id__icontains=q)|Q(S_name__icontains=q)|Q(S_branch__icontains=q))
        if (q=='A' or q=='B'):
            POST=Students.objects.filter(Q(S_category__icontains=q))
    else:
        POST=Students.objects.all()
    #POST=classes.objects.filter(C_id="20FE1A1236")
    data={
        'data':POST
    }
    return render(request,'base.html',data)
def simple_upload(request):
    if request.method=='POST':
       file2=request.FILES["file"]
       document=FilesUpload.objects.create(file=file2)
       document.save()
       return HttpResponse("Your file was uploaded")
    return render(request,'upload.html')
# views.py
#from django.shortcuts import render
#from .models import YourModel  # Replace "YourModel" with the actual name of your mode
def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            max_value = form.cleaned_data['max_value']
            results =Students.objects.filter(S_due__lt=max_value)
        else:
            results = []
    else:
        form = SearchForm()
        results = []

    return render(request, 'search.html', {'form': form, 'results': results})
from django.contrib.auth import authenticate, login
from django.shortcuts import  redirect

def login_view(request):
    if request.method == 'POST':
        student_id = request.POST['college_id']
        password = request.POST['password']
        user = authenticate(request, username=student_id, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000')  # Redirect to the dashboard page upon successful login
        else:
            error_message = 'Invalid credentials. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')
# views.py
from django.shortcuts import get_object_or_404

def detail_page(request,pk):
    pk='20FE1A1236'
    ref= get_object_or_404(Students, pk=pk)
    return render(request, 'students_full.html', {'ref': ref})


