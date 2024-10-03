from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('biomas/', views.biomas_view, name='biomas'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('resultados/', views.resultados_view, name='resultados'),
]
