from django.forms import ModelForm, fields
from .models import Release

class ReleaseForm(ModelForm):
  class Meta:
    model = Release
    fields = ["date", "enjoy"]