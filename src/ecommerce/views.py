from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	context = {
		"title":"still working hard",
		"content":"Welcome to the technology hub to the future"
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title":"About us",
		"content":"Welcome to the about page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	context = {
		"title":"Contact Us",
		"content":"Welcome to the contact page"
	}
	if request.method == "POST":
		print(request.POST)
	return render(request, "contact/view.html", context)




	
