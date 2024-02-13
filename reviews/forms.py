from django import forms
from .models import Review
class ReviewForm(forms.Form):
    user_name=forms.CharField(max_length=100,label="Your Name",error_messages={
        "required":"Your username can't be empty",
        "max_length":"Don't write such long usernames"
    }) 
    feed_back=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=1000)
    rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)
class Reviewdb(forms.ModelForm):
    class Meta:
        model = Review
        fields='__all__'
        labels={
            'user_name':'Your Name',
            "review_text":'Your Feedback',
            'rating':'Your Rating'
        }
        error_messages={
            "user_name":{
                "required":"Your username can't be empty",
                "max_length":"Don't write such long usernames"
            }
        }
