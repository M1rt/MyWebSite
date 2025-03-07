from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User, Word
from django.views.generic import DeleteView
from .forms import WordForm



class UserDeleteView(DeleteView):
    model = User
    success_url = '..'
    template_name = 'moderator/user_delete.html'

def show_index(request):
    return render(request, "moderator/index.html")

def show_users(request):
    users = User.objects.all()
    return render(request, "moderator/user.html", {"users":users})


def create_word(request):
    return request(request, 'moderator/word_create.html')
def show_word(request):
    words = Word.objects.all()
    return render(request, 'moderator/words.html',  {"words": words})




