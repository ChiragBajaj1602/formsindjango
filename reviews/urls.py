from django.urls import path
from . import views
urlpatterns = [
    path('',views.reviewView.as_view()),
    path('ThankYou',views.Thankspage)
]
