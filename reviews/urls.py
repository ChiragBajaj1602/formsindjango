from django.urls import path
from . import views
urlpatterns = [
    path('',views.Formsubmission1.as_view()),
    path('ThankYou',views.ThankYouView.as_view()),
    path('All',views.AllReviews.as_view()),
    path('reviews/<int:pk>',views.DetailViewsReviews.as_view())
]
