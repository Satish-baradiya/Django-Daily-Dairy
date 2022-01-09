from django import forms
from django.forms import ModelForm
from .models import Entry


class TaskForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form