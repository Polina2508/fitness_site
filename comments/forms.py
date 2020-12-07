from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name","email","text")