# Done by Carlos Amaral (2021/01/02)

from django.urls import path

from .views import editor, delete_document

urlpatterns = [
    path('', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
]
