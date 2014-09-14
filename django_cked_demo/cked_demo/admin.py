from django.contrib import admin
from django.forms import CharField, ModelForm
from cked.widgets import CKEditorWidget
from .models import Article

class ArticleForm(ModelForm):
    text = CharField(widget=CKEditorWidget)

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)
