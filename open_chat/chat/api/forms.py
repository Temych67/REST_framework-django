from django import forms
from chat.models import Chat

class AccountAuthenticationForm(forms.ModelForm):

	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
	message = froms.TextField(max_length=100,null=False)
	class Meta:
		model = Chat
		fields = ('email', 'message')