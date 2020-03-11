import json
from django.http import HttpResponse
from django.shortcuts import render
from headLanding.models import Contacts
from voice_email.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def results(request):
    if request.method == 'POST':
        cname = request.POST['contactname']
        cnts = Contacts.objects.filter(contact_name=cname)
        cemail = []
        for c in cnts:
            cemail.append(c.contact_email)
        if len(cemail) == 1:
            return render(request, 'results.html', {'name': cname, 'email': cemail[0], 'len': len(cnts)})
        else:
            return render(request, 'results.html', {'name': cname, 'email': cemail, 'len': len(cnts)})
    else:
        return render(request, 'results.html')


def sendmail(request):
    if request.method == 'POST':
        subject = request.POST['msub']
        message = request.POST['editordata']
        recepient = [request.POST['cemail']]
        send_mail(subject, 'hi', EMAIL_HOST_USER, recepient,
                  html_message=message, fail_silently=False)
        return render(request, 'mail.html')


def addcontact(request):
    message = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        obj = Contacts.objects.create(contact_name=name, contact_email=email)
        obj.save()
        message = "Sucessfully Added"
    return render(request, 'addcontact.html', {'mess': message})


def ajaxForm(request):
    if request.method == 'POST':
        print(request.POST['name'])
        if request.POST['name'] == 'Abhinandan pk':
            return HttpResponse("Abhinandan Purkait")
        else:
            return HttpResponse(request.POST['name'])
    return render(request, 'ajax.html')
