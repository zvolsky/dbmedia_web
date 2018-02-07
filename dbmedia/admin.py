from .models import Obrazek
from db_file_storage.form_widgets import DBAdminClearableFileInput
from django import forms
from django.contrib import admin


class Form_Obrazek(forms.ModelForm):
    class Meta:
        model = Obrazek
        exclude = []
        widgets = {
            'obrazek': DBAdminClearableFileInput
        }

class ConsoleAdmin(admin.ModelAdmin):
    form = Form_Obrazek


admin.site.register(Obrazek)
