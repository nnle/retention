# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


from frontend.models import Navibar, Post, Course

import os
import csv
import datetime as dt
#reverse("includes/navigation.html", pages=("home" , "Home"))
# Create your views here.

# Generate counts of some of the main objects

def index(request, lang = 'vn'):
    try:
        if lang == 'vn':
            label_navibar = Navibar.objects.filter(lang = 0) # VN
        else:
            label_navibar = Navibar.objects.filter(lang = 1) # EN            
    except Navibar.DoesNotExist:
        raise Http404("Navibar does not exist")
        
    for p in label_navibar:
        p.clean()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'label_navibar' : label_navibar,
        'vn': lang,
        'num_visits': num_visits,
    }
    return render(request, "tech/index.html", context = context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def courses(request, lang = 'vn'):
    try:
        if lang == 'vn':
            label_navibar = Navibar.objects.filter(lang = 0) # VN
        else:
            label_navibar = Navibar.objects.filter(lang = 1) # EN
    except Navibar.DoesNotExist:
        raise Http404("Navibar does not exist")
    
    try:
        courses = Course.objects.all()        
    except Course.DoesNotExist:
        raise Http404("Course does not exist")


    context = {
        'label_navibar' : label_navibar,
        'courses' : courses,
        'vn': lang,
    }

    #return render(request, "tech/upload.html", context = context)    
    return render(request, "tech/courses.html", context = context)    

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg','cpp', '.zip'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload(request, lang = 'vn', courseName = None):
    
    #print(APP_ROOT)
    #print(UPLOAD_FOLDER)
    #print(courseName)
    try:
        if lang == 'vn':
            label_navibar = Navibar.objects.filter(lang = 0) # VN
        else:
            label_navibar = Navibar.objects.filter(lang = 1) # EN
    except Navibar.DoesNotExist:
        raise Http404("Navibar does not exist")

    context = {
        'label_navibar' : label_navibar,    
        'vn': lang,
    }
    context["courseName"] = courseName 
    
    if request.method == 'POST':   
            
        target = os.path.join(UPLOAD_FOLDER, courseName)
        print(target)

        # Create a form instance and populate it with data from the request (binding):
        
        if not os.path.isdir(target):
            os.mkdir(target)
        else:
            print("Couldn't create upload directory: {}".format(target))
        # check if the post request has the file part                
        
        for file in request.FILES.getlist("file_ans"):        
            #file = request.files["file_ans"]
            print(file.name)
            # if user does not select file, browser also
            # submit an empty part without filename
                        
            #filename = secure_filename(file.filename)
            #destination = "/".join([target, filename])
            
            destination = os.path.join(target, '_'.join([request.POST['mssv'],file.name]))            
            #print(destination)            
            #path = default_storage.save(destination, ContentFile(file.read()))
            fs = FileSystemStorage(target)
            filename = fs.save('_'.join([request.POST['mssv'],file.name]), file)

            print("Image saved")                    
         
        
        filePath = os.path.join(target, dt.datetime.now().year.__str__().join([courseName, '.csv'])) 
        
        fieldnames = ['MSSV', 'Email', 'Fullname']
            
        if not os.path.isfile(filePath):                
            with open(filePath, 'w', newline='', encoding="utf8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()                
                writer.writerow({'MSSV': request.POST['mssv'], 'Email': request.POST['email'], 'Fullname':request.POST['fullname']})
        else:
            with open(filePath, 'a', newline='', encoding="utf8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'MSSV': request.POST['mssv'], 'Email': request.POST['email'], 'Fullname':request.POST['fullname']})
        #Sprint(context)                                                                     
        #return render(request, "tech/upload.html", context = context)
            
    #else:                
        
        #if courseName is None:
            
        #    return render(request, "error.html", {"message":"No exist the course."})
        #else: 
            # Make sure flight cd exists.
        #    course = Course.objects.filter(coursename=courseName).all()
            
        #    if course is None:
        #        return render(request, "tech/error.html", {"message":"No such flight."})
         
        #print(context) 
    return render(request, "tech/upload.html", context = context)
      
    
    #return HttpResponse('Hello, World!')


def home(request, page_id, lang = 'vn'):
    try:
        if lang == 'vn':
            label_navibar = Navibar.objects.filter(lang = 0) # VN            
        else:
            label_navibar = Navibar.objects.filter(lang = 1) # EN              
            posts = Post.objects.filter(navibar=page_id)

    except Navibar.DoesNotExist:
        raise Http404("Navibar does not exist")
    
    try:
        #posts = Post.objects.all()      
        posts = Post.objects.filter(navibar=page_id)
        #Post.objects.exclude(flights=flight).all()
        #flight = Navibar.objects.get(pk=flight_id)

    except Course.DoesNotExist:
        raise Http404("Course does not exist")


    context = {
        'label_navibar' : label_navibar,
        'posts' : posts,
        'vn': lang,
    }

    #return render(request, "tech/upload.html", context = context)    
    return render(request, "tech/home.html", context = context)    
