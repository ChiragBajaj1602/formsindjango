from django.urls import path
from . import views
urlpatterns = [
    path('',views.reviewView.as_view()),
    path('ThankYou',views.ThankYouView.as_view()),
    path('All',views.AllReviews.as_view()),
    path('reviews/<int:id>',views.singlereviewlist.as_view())
]
