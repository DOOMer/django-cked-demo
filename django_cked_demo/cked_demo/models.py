from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    text = models.TextField(max_length=16536, verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"
        ordering = ('-created',)

    def _str_(self):
        return self.title
