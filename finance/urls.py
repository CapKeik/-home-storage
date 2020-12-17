from django.conf.urls import url
from django.urls import path


from . import views

app_name = 'finance'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('<int:user_id>/', views.profile, name='profile'),
    path('<int:user_id>/add_category/', views.add_category, name='add_category'),
    path('<int:user_id>/add_category/', views.add_category, name='add_category')
]
