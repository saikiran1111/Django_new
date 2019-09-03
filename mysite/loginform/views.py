from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import requests

def home(request):
	count =User.objects.count()
	return render(request,'home.html',{
		'count':count
		})




def index(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request, "index.html", data)

def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=8"

    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()

    return data


def bot(request):

	
	return render(request,'bot.html')

def exchange(request):
	
	return render(request,'exchange.html')


def logo(request):
	
	return render(request,'logo.html')


def signup(request):
	if request.method =='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{
		'form':form
		})
