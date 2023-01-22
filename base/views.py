from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import poetry, category, comments
from .forms import poemForm, SignUpForm, UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# view for login


def loginPage(request):
    form = SignUpForm()
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is wrong')
    context = {'form': form}
    return render(request, 'base/login_register.html', context)

# view for logout


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

# view for SignUp


def registration(request):
    page = 'register'
    form = SignUpForm(request.POST)
    context = {'form': form, 'page': page}

    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('home')
    else:

        error = [form.errors[key] for key in form.errors][0][0]

        print(type(error))
        messages.error(request, error)
        return render(request, 'base/login_register.html', context)

# view for Index_page


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    all_ = poetry.objects.all()
    count = all_.count()
    Poetry = poetry.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(Author__username__icontains=q)
    )
    p = Paginator(Poetry, 6)

    recent_p = all_[:3]

    page_number = request.GET.get(
        'page') if request.GET.get('page') != None else '1'
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_number = '1'
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_number = p.num_pages
        page_obj = p.page(p.num_pages)
    if page_number == '1':
        poem_count = Poetry.count()
        categorys = category.objects.all()
        context = {'Poetry': Poetry, 'categorys': categorys, 'poem_count': poem_count,
                   'count': count, 'page_obj': page_obj, 'recent_p': recent_p}
        return render(request, 'base/index.html', context)
    else:
        poem_count = Poetry.count()
        categorys = category.objects.all()
        context = {'Poetry': Poetry, 'categorys': categorys, 'poem_count': poem_count,
                   'count': count, 'page_obj': page_obj, 'recent_p': recent_p}
        return render(request, 'base/sec_index.html', context)

# view for Search_page


def search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    all_ = poetry.objects.all()
    count = all_.count()
    Poetry = poetry.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(Author__username__icontains=q)
    )
    p = Paginator(Poetry, 5)
    recent_p = all_[:3]
    categorys = category.objects.all()
    if Poetry.count() == 0:
        return render(request, 'base/nothing.html', {'q': q, 'recent_p': recent_p, 'categorys': categorys, 'count': count})
    recent_p = all_[:3]

    page_number = request.GET.get(
        'page') if request.GET.get('page') != None else '1'
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_number = '1'
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_number = p.num_pages
        page_obj = p.page(p.num_pages)

    context = {'Poetry': Poetry, 'categorys': categorys, 'count': count,
               'q': q, 'recent_p': recent_p, 'page_obj': page_obj}
    return render(request, 'base/search.html', context)

# view to fetch categories and no. of poems in it


def categorys(request):
    all_ = poetry.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    count = poetry.objects.all().count()
    Poetry = poetry.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(Author__username__icontains=q)
    )
    p = Paginator(Poetry, 5)

    recent_p = all_[:3]

    page_number = request.GET.get(
        'page') if request.GET.get('page') != None else '1'
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_number = '1'
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_number = p.num_pages
        page_obj = p.page(p.num_pages)
    poem_count = Poetry.count()
    categorys = category.objects.all()
    context = {'Poetry': Poetry, 'categorys': categorys, 'poem_count': poem_count,
               'count': count, 'q': q, 'recent_p': recent_p, 'page_obj': page_obj}
    return render(request, 'base/category.html', context)

# view for author hyperlinks


def author(request):
    all_ = poetry.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    count = poetry.objects.all().count()
    Poetry = poetry.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(Author__username__icontains=q)
    )
    p = Paginator(Poetry, 5)

    recent_p = all_[:3]

    page_number = request.GET.get(
        'page') if request.GET.get('page') != None else '1'
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_number = '1'
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_number = p.num_pages
        page_obj = p.page(p.num_pages)
    poem_count = Poetry.count()
    categorys = category.objects.all()
    poem_count = Poetry.count()
    categorys = category.objects.all()
    context = {'Poetry': Poetry, 'categorys': categorys, 'poem_count': poem_count,
               'count': count, 'q': q, 'recent_p': recent_p, 'page_obj': page_obj}
    return render(request, 'base/author.html', context)

# view for main poem content


def poem(request, slug):
    Poetry = poetry.objects.get(id=slug)
    Comments = Poetry.comments_set.all().order_by('-created')

    if request.method == 'POST':
        comment = comments.objects.create(
            user=request.user,
            poetry=Poetry,
            body=request.POST.get('body')


        )
        return redirect('poem', slug=Poetry.id)
    count = str(Comments.count())
    context = {'Poetry': Poetry, 'comments': Comments, 'count': count}
    return render(request, 'base/poem.html', context)

# view for creating new Poems


@login_required(login_url='login')
def createForm(request):
    page = 'create'
    form = poemForm()
    categorys = category.objects.all()

    if request.method == 'POST':

        poem_category = request.POST.get('category')
        cate_old, created = category.objects.get_or_create(name=poem_category)
        poetry.objects.create(
            Author=request.user,
            name=request.POST.get('name'),
            category=cate_old,
            content=request.POST.get('content'),
        )

        return redirect('home')
    context = {'form': form, 'categorys': categorys, 'page': page}

    return render(request, 'base/poem_form.html', context)

# view for updating Poems


@login_required(login_url='login')
def updatePoem(request, slug):
    Poetry = poetry.objects.get(id=slug)
    form = poemForm(instance=Poetry)
    categorys = category.objects.all()
    if request.user != Poetry.Author:
        return HttpResponse('You are not allowed here')
    if request.method == 'POST':

        poem_category = request.POST.get('category')
        cate_old, created = category.objects.get_or_create(name=poem_category)

        Poetry.name = request.POST.get('name')
        Poetry.category = cate_old
        Poetry.content = request.POST.get('content')
        Poetry.save()
        return redirect('home')

    context = {'form': form, 'poem': Poetry, 'categorys': categorys}
    return render(request, 'base/poem_form.html', context)

# view for deleting poem if request.auth.user == poem.author


@login_required(login_url='login')
def deletePoem(request, slug):
    Poetry = poetry.objects.get(id=slug)

    if request.user != Poetry.Author:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        Poetry.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': Poetry})

# view for deleting comments


@login_required(login_url='login')
def deleteMessage(request, slug):

    comment = comments.objects.get(id=slug)

    if request.user != comment.user:

        return HttpResponse('You are not allowed here')

    if request.method == 'POST':

        comment.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': comment})

# view for about us page uses about.txt for body content


def about_us(request):

    about = open('C:/Users/alisa/Desktop/ReadSomePoems/base/about.txt').read()
    context = {'about': about}
    return render(request, 'base/about.html', context)
