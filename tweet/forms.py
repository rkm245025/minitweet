from django import forms
from .models import Tweet,Contactus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    photo=forms.ImageField()
    class Meta:
        model=Tweet
        fields=['text','photo']


    def __init__(self,*args,**kwargs):
        super(TweetForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs['class'] = 'textarea'
        self.fields['text'].widget.attrs['placeholder'] = 'Enter your tweet!'

        self.fields['photo'].widget.attrs['class'] = 'file-input'



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'input'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'input'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'input'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
            


class ContactUsForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=("name","info","email","mobile")
    def __init__(self,*args,**kwargs):
          super(ContactUsForm,self).__init__(*args,**kwargs)
          self.fields['name'].widget.attrs['class'] = 'input'
          self.fields['info'].widget.attrs['class'] = 'textarea'
          self.fields['email'].widget.attrs['class'] = 'input'
          self.fields['mobile'].widget.attrs['class'] = 'input'
            

	