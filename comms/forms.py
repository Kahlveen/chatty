from django import forms

class MsgForm(forms.Form):
	send_msg = forms.CharField(label="", max_length=200)
	
