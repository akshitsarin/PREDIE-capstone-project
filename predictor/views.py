from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request, *args, **keywordargs):
	return render(request, 'welcome.html', {})

def about_view(request, *args, **keywordargs):
	return render(request, 'about.html', {})


def contact_view(request, *args, **keywordargs):
	return render(request, 'contact.html', {})

def team_view(request, *args, **keywordargs):
	return render(request, 'team.html', {})

def predict_view(request, *args, **keywordargs):
	return render(request, 'predict.html', {})

def result_view(request, *args, **keywordargs):
	return render(request, 'result.html', {})

def test_view(request, *args, **keywordargs):
	return render(request, 'test_page.html', {})