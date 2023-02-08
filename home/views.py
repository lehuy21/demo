from django.shortcuts import render
from .models import UserModel
from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def index (request):
    return render(request, 'auth/index.html')

def about (request):
    return render(request, 'informations/about.html')

def blog (request):
    return render(request, 'informations/blog.html' )

def contact (request):
    return render(request, 'informations/contact.html')

def featured (request):
    return render(request, 'informations/featured.html' )

# def success(request):
#     email = request.POST.get('email', '')
#     data = """
#         Hello! I am Phuc.
#     """
#     send_mail('Welcome!', data, "PLC", [email], fail_silently=False)
#     return render(request, 'send_email/success.html')
# def main(request):
#     return render(request, 'send_email/main.html')

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["lhuy211102@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact")
    return render(request, "informations/contact.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")