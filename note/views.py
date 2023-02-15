from rest_framework import viewsets, status
from rest_framework.response import Response

from note.models import Note
from note.serializers import NoteSerializer


class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.filter()
    serializer_class = NoteSerializer
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']

