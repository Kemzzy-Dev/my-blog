from django.shortcuts import render, redirect
from .models import *
from .forms import newsletter, contactForm, newsletterForm
from django.conf import settings
from django.core.paginator import Paginator
from django.core.mail import send_mail


# Create your views here.

def index(request):

    posts = post.objects.all().order_by('-created_on').filter(status=1)[:5]
    sidebar = post.objects.all().order_by('-created_on')[:6]

    context = {
        'posts':posts,
        'sidebar':sidebar,
    }

    return render(request, 'website/index.html', context)

def about(request):
    suscribe_form = newsletterForm()
    return render(request, 'website/about.html', {'form':suscribe_form})

def blog(request):
    posts = post.objects.all().order_by('-created_on').filter(status=1)
    sidebar_posts = posts[:6]
    suscribe_form = newsletterForm()
    search_value = request.GET.get('q')
    
    if search_value != None:
        posts = post.objects.all().order_by('-created_on').filter(status=1, tags__name=search_value)
        
 # In order to use the paginator we have to set the paginator to the object post and 
    # use paginator on the page
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'sidebar':sidebar_posts,
        'posts': page_obj
    }
    return render(request, 'website/blog.html', context)
    
def contacts(request):

    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()

            user = contact.objects.latest('id')
            subject = user.subject
            message = (user.message)
            email_from = user.email
            recipient_list = [settings.EMAIL_HOST_USER, ]
            send_mail( subject, message, email_from, recipient_list )

            return redirect('/')
    else:
        form = contactForm()


    return render(request, 'website/contact.html', {'form':form,})

def details(request, slug):
    suscribe_form = newsletterForm()
    view_posts = post.objects.get(slug=slug)
    sidebar = post.objects.all().order_by('-created_on').filter(status=1)[:6]

    if request.method == 'POST':
        suscribe_form = newsletterForm(request.POST)
        if suscribe_form.is_valid():
            suscribe_form.save()

            suscribed_mail = newsletter.objects.latest('id')

            subject = "Successful suscription"
            message = ("Thank you for suscribing to our daily newsletter")
            email_from = settings.EMAIL_HOST_USER
            print(email_from)
            recipient_list = [suscribed_mail.email, ]
            send_mail( subject, message, email_from, recipient_list )

            return redirect('/')
            

    context = {
        'view_posts':view_posts,
        'sidebar':sidebar,
        'form':suscribe_form
    }
    
    return render(request, 'website/details.html', context)

def category(request, str):
    sidebar = post.objects.all().order_by('-created_on').filter(status=1)[:6]
    category = post.objects.filter(category=str.upper())

    paginator = Paginator(category, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'website/category.html', {'category':page_obj, 'sidebar':sidebar})

def drafts(request):
    draft_posts = post.objects.all().order_by('-created_on').filter(status=0)
    return render(request, 'website/drafts.html', {'draft_post': draft_posts} )