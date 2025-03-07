from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.show_index, name="index"),
    path('<int:user_id>/account', views.show_account, name="account"),
    path('login/', views.show_login, name="login"),
    path('create', views.show_create, name="create"),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name="user_update"),
    path("<int:user_id>/aboutus/", views.aboutus, name="aboutus"),
    path('<int:user_id>/word/', views.word, name='word'),
    path('<int:user_id>/show_user_create/', views.show_user_create, name="show_user_create"),
]

