from django.urls import path
from . import views
urlpatterns = [
    path("",views.createProfileView.as_view()),
    path('profile',views.createprofile.as_view()),
    path('All',views.listprofile.as_view())
]

