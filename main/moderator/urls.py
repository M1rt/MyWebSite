from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="index"),
    path('create', views.create_word, name="create"),
    path('users/', views.show_users, name="show_users"),
    path('users/<int:pk>/delete', views.UserDeleteView.as_view(), name="user_delete"),
    path('words', views.show_word, name='words')

]



