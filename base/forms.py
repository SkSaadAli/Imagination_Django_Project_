from django.forms import ModelForm
from .models import poetry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#using model form with little customization


#model form for poem mainly used for poem creating or updation
class poemForm(ModelForm):
    class Meta:
        model =poetry
        fields = '__all__'
        exclude=['Author']

#model form for SignUp form
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder':'Username'
        })
        
        self.fields['password1'].widget.attrs.update({
            'placeholder':'password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder':'confirm password'
        })
    class Meta:
        model = User 
        fields = ['username','password1','password2']

