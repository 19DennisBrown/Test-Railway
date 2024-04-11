from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('userdelete/', views.delete_user_view, name='userdelete'),

    # //crud
    path('profile/loan/', views.view_loan, name='view_profile'),
    path('profile/update/', views.update_loan, name='update_loan'),
    path('profile/delete/<int:id>/', views.delete_loan, name='delete_loan'),
    path('profile/create/', views.create_loan, name='create_loan'),
]
