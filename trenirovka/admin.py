from django import forms
from django.contrib import admin
from .models import Trenirovka
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category

admin.site.register(Category)

class TrenirovkaAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Trenirovka
        fields = '__all__'

@admin.register(Trenirovka)
class TrenirovkaAdmin(admin.ModelAdmin):
    """Фильмы"""
    form = TrenirovkaAdminForm





