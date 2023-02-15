from django.urls import path, include
from rest_framework import routers

from note.views import NoteViewset

router = routers.DefaultRouter()
router.register('note', NoteViewset)

urlpatterns = [
    path('', include(router.urls)),
]
