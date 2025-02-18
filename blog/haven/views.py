from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required


from .models import *
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string



def index(request):
    recent_posts = Article.objects.all().order_by('-date')[:4]  

    context = {
        'recent_posts': recent_posts,
    }
    return render(request, "index.html", context)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.all().filter(article=article)
    forms = CommentForm()
    if request.method == "POST":
        forms = CommentForm(request.POST)
        if forms.is_valid():
            comment = forms.save(commit = False)
            comment.article = article
            comment.user = request.user
            comment.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                data = {
                    'username': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime("%b %d, %Y - %H:%M"),
                    'success': True
                }
                return JsonResponse(data)
            return redirect("article_detail", id=id)
        else:
            forms = CommentForm()
    return render(request, "article_detail.html", {"article": article, "comments": comments, "forms": forms}  )

@login_required(login_url="login")
def blog(request, slug=None):
    current_category = None
    articles = None
    if slug:
        current_category = get_object_or_404(Categories, slug=slug)
        articles = Article.objects.filter(categorys=current_category).order_by('-date')
    else:
        articles = Article.objects.all().order_by('-date')

    categorys = Categories.objects.all()

    post_form = PostForm()

    if request.method == "POST" and "article_id" in request.POST:
        article_id = request.POST.get("article_id")
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            article.like_count -= 1
            liked = False
        else:
            article.likes.add(request.user)
            article.like_count += 1
            liked = True
        article.save()
        return JsonResponse({
            "liked": liked,
            "like_count": article.like_count,
        })

    if request.method == "POST" and "create_post" in request.POST:
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            # if slug:
            #     return redirect('blog_with_slug', slug=slug)
            # else:
            return redirect('blog')            

    context = {
        'current_category': current_category,
        'categorys': categorys,
        'articles': articles,
        'post_form': post_form,
    }
    return render(request, "blog.html", context)




def about(request):
    return render(request, "about.html")

def contact(request):
    faqs = FAQ.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Feedback.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")  # Redirects to the `contact` view

    return render(request, "contact.html", {"faqs": faqs})

def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)



def registerPage(request):
    form = CreateuserForm()
    if request.method == "POST":
        form = CreateuserForm(request.POST)
        if form.is_valid():
            user = form.save()  
            context = {
                'username': user.username,
                'email': user.email,
                'message': "Thank you for registering with us! We are happy to have you on board."
            }
            html_message = render_to_string('email.html', context)

            send_mail(
                'Welcome to Our Website!',  
                '',
                settings.EMAIL_HOST_USER,  
                [user.email],  
                fail_silently=False,
                html_message=html_message  
            )
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@login_required(login_url="login")
def logoutPage(request):
    auth.logout(request)
    return redirect("index")