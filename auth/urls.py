from django.urls import path
from .views import register,Dashboard_view,login_view,logout_view

urlpatterns = [
    path('', register, name='Register'),
    path('Home/', Dashboard_view, name='Dashboard'),
    path('Login/', login_view, name='Login'),
    path('Logout/', logout_view, name='Logout'),
]
