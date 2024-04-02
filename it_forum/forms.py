from django import forms
from it_forum.models import ItForum, ReviewForum


class ItForumForm(forms.ModelForm):
    class Meta:
        model = ItForum
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewForum
        fields = '__all__'
