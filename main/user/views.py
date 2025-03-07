from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import UpdateView
from moderator.forms import WordForm
from .forms import UserForm
from .models import Word, User

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/create.html'
    form_class = UserForm
    success_url = "../.."

def show_index(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "user/index.html",{'user':user})

def show_account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "user/account.html",{'user':user, "user_id":user_id})



def show_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return redirect('index', user_id = user.id)
        except:
            return render(request, 'user/login.html')

    return render(request, "user/login.html")

def show_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('..')
    form = UserForm()
    data = {'form': form}
    return render(request, "user/create.html", data)

def aboutus(request, user_id):
    return render(request, "user/aboutus.html", {"user_id": user_id})

def word(request, user_id):
    words = Word.objects.all()
    query = request.GET.get('q', '')  # Получаем параметр поиска
    if query:
        words = Word.objects.filter(Slovo__icontains=query)
    else:
        words = Word.objects.all()
    return render(request, "user/word.html", {"words": words, "user_id": user_id})

def show_user_create(request, user_id):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word', user_id=user_id)
    else:
        form = WordForm()
    return render(request, 'user/word_create.html', {'form': form, 'user_id': user_id})




