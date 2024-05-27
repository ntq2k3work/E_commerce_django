from django.urls import path
from userauths.views import register_view,login_view

app_name = 'userauths'

urlpatterns = [
    path('sign-up/',view=register_view,name='sign-up'),
    path('sign-in/',view=login_view,name='sign-in'),
]