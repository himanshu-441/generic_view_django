from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from main import models
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.


class Index(View):
    def get(self, request):
        return HttpResponse('GET request')
    
    def post(self, request):
        return HttpResponse('POST request')
    

class CollegeDetail(DetailView):
    model = models.College
    template_name = 'college_detail.html'

class CollegeList(ListView):
    model = models.College
    template_name = 'college_list.html'
    context_object_name = 'colleges'

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'college_create.html'
    fields = "__all__"
    success_url= '/college'


    def get_absolute_url(*args, **kwargs):
        return '/'
    

class StudentCreate(CreateView):
    model = models.Student
    template_name = 'student_create.html'
    fields = '__all__'
    success_url = '/'

class CollegeUpdate(UpdateView):
    model = models.College
    template_name = 'college_create.html'
    fields = "__all__"
    success_url= '/college'

class StudentDelete(DeleteView):
    model = models.Student
    template_name = 'confirm.html'
    success_url = '/'


    
#django provides five generic views 
#detail view
#list view
#create view
#update view
#delete view



