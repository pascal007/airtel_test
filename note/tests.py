from rest_framework import status
from rest_framework.test import APITestCase

from note.models import Note


class TestCreateNote(APITestCase):

    def test_create_note_authenticated_user(self):
        data = {"title": "This is a test title", "description": "This describes the task"}
        note_count = Note.objects.all().count()
        response = self.client.post('/note/', data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'This is a test title')
        self.assertEqual(response.data['description'], "This describes the task")
        self.assertEqual(Note.objects.all().count(), note_count + 1)

    # def test_create_note_unauthenticated_user(self):
    #     data = {"title": "This is a test title", "description": "This describes the task"}
    #     response = self.client.post('/note/', data, follow=True)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_list_note_authenticated_user(self):
    #     response = self.client.get('/note/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
