# Done by Carlos Amaral (2021/01/01)

from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)  # with null and blank fields set to true,
    # we can write a document with a title but with no content

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
