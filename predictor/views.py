from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request, *args, **keywordargs):
	return render(request, 'welcome.html', {})