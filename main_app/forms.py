from django.forms import ModelForm, fields
from .models import Release

class ReleaseFor(ModelForm):
  class Meta:
    model = Release
    fields = ["date", "enjoy"]