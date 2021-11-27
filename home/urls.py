from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('signup/', views.signUp, name='signUp'),
    path('changepass/', views.changePassword, name='changePassword'),
    path('editprofile/', views.editProfile, name='editProfile'),
    path('assignment/', views.assignment, name='assignment'),
    path('feespayment/', views.feePayment, name='feePayment'),
    path('knowledgecenter/', views.knowledgeCenter, name='knowledgeCenter'),
]