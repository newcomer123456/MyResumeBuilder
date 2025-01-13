from django.urls import path
from auto import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('detail-user/<pk>/', views.UserDetailView.as_view(), name='detail-user'),
    path('update-user/<pk>/', views.UserUpdateView.as_view(), name='update-user'),
    path('delete-user/<pk>/', views.UserDeleteView.as_view(), name='delete-user'),
    path('', views.HomepageTemplateView.as_view(), name='homepage'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]