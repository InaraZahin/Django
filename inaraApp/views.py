from django.shortcuts import render, redirect

# Create your views here.

from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView, TemplateView

import requests
from django.shortcuts import render, get_object_or_404

from .models import Post
from .models import Message
from .forms import ContactUsForm




from .models import Home
from .models import Hero
from .models import Abt
from .models import Proc
from .models import Whyus
from .models import Team
from .models import Works
from .models import Testi
from .models import Blog
from .models import Callaction
from .models import Post
def index(request):
    home = Home.objects.all().filter(is_published=True)
    hero = Hero.objects.all().filter(is_published=True)
    abt = Abt.objects.all().filter(is_published=True)
    proc = Proc.objects.all().filter(is_published=True)
    whyus = Whyus.objects.all().filter(is_published=True)
    team = Team.objects.all().filter(is_published=True)
    works = Works.objects.all().filter(is_published = True)
    testi = Testi.objects.all().filter(is_published=True)
    blog = Blog.objects.all().filter(is_published=True)
    action = Callaction.objects.all().filter(is_published=True)
    post = Post.objects.all()
    context = {
        'home': home,
        'hero': hero,
        'abt': abt,
        'proc': proc,
        'whyus': whyus,
        'team': team,
        'works': works,
        'testi': testi,
        'blog': blog,
        'action': action,
        'post': post,

    }




    return render(request, 'index.html', context)


def new_index(request):


    return render(request, 'chimper/index.html')
def about(request):


    return render(request, 'chimper/about.html')
def blog(request):


    return render(request, 'chimper/blog.html')
def contact(request):


    return render(request, 'chimper/contact.html')
def services(request):


    return render(request, 'chimper/services.html')
def work(request):


    return render(request, 'chimper/work.html')
def worksingle(request):


    return render(request, 'chimper/work-single.html')


class ContactView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "Heartcare Contact"

        if name and message and email and phone:
            send_mail(
                subject+"-"+name,
                message+"\n \n \n Name: "+name+" \n Email Address: "+email+" \n Phone Number: "+phone,
                phone,

                ['ariful.islamk777@gmail.com', 'inarazahin@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, " Email hasbeen sent successfully...")

            form = ContactUsForm(request.POST or None)

            errors = None
            if form.is_valid():
                form.save()
                return redirect("/")
            if form.errors:
                errors = form.errors
            context = {
                "form": form,
            }

        return redirect('container')

# def createpost(request):
#     if request.method == 'POST':
#         if request.POST.get('title') and request.POST.get('content'):
#             post = Post()
#             post.title = request.POST.get('title')
#             post.content = request.POST.get('content')
#             post.save()
#
#             return render(request, 'posts/create.html')
#
#     else:
#         return render(request, 'posts/create.html')

# def createmessage(request):
#     if request.method == 'POST':
#         if request.POST.get('name') and request.POST().get('content') and request.POST.get('email'):
#             message = Message()
#             message.name = request.POST.get('name')
#             message.content = request.POST.get('content')
#             message.email = request.POST.get('email')
#             message.save()
#
#             return render(request, 'index.html')
#
#     else:
#         return render(request, 'index.html')


def createpost(request):
    # if request.method == 'POST':
    #     if request.POST.get('title') and request.POST.get('content'):
    #         post = Post()
    #         post.title = request.POST.get('title')
    #         post.content = request.POST.get('content')
    #         post.save()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']


        savedata = Post(name=name, email=email, phone=phone, subject=subject,
                          message=message)

        savedata.save()

        return redirect('/')




