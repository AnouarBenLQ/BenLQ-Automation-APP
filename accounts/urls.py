from django.urls import path
from . import views


app_name="accounts"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView, name='logout'),
    path('userprofile/', views.UserProfileView.as_view(), name='userprofile'),
]
