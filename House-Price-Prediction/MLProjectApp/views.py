from django.shortcuts import render, HttpResponse
from datetime import datetime
from MLProjectApp.admin import Contact
from django.contrib import messages
import pandas as pd
import pickle
import numpy as np

data = pd.read_csv("Cleaned_data.csv")
pipe = pickle.load(open("RidgeModel.pkl",'rb'))

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def predict(request):
    locations = sorted(data['location'].unique())
    context = {
                   'locations':locations
            }
    return render(request, 'predict.html', context)

def prediction(request):
    if request.method == "POST":
        location = request.POST.get('location') 
        bhk = request.POST.get('bhk')
        bath = request.POST.get('bath')
        sqft = request.POST.get('total_sqft')
        print(location,bhk,bath,sqft)
        input1 = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
        prediction = pipe.predict(input1)[0] * 1e5
        prediction = str(np.round(prediction,2)) 
        return HttpResponse('<h1>'+prediction+'</h1>')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        type_choice = request.POST.get('type_choice')
        desc = request.POST.get('desc')
        error_message = None
        # Validation

        if(not name):
            error_message = "Name Required!!"
        elif(len(name)<4):
            error_message = "Name Must Have Atleast 4 Character!!"
        elif(len(phone)<10):
            error_message = "Phone Number Must Have Atleast 10 Digits!!"
        elif(not phone.isnumeric()):
            error_message = "Phone Number Must Be Numeric!!"

        # Saving
        if(not error_message):
            contact = Contact(name=name, email=email, phone=phone, type_choice=type_choice, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, 'Your message has been sent!')
        else:
            return render(request, 'contact.html', {'error': error_message})
    return render(request, 'contact.html')