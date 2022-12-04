from django.test import TestCase
from .models import YambScores
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the yamb scores model"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.yambScores_player1_name = "Milan"
        self.yambScores_player1_score = 500
        self.yambScores_player2_name = "Emma"
        self.yambScores_player2_score = 600
        self.yambScores = YambScores(
            player1_name=self.yambScores_player1_name, 
            player1_score=self.yambScores_player1_score, 
            player2_name=self.yambScores_player2_name, 
            player2_score=self.yambScores_player2_score)

    def test_model_can_create_a_yamb_score(self):
        """Test the yamb score model can create a yamb score"""
        old_count = YambScores.objects.count()
        self.yambScores.save()
        new_count = YambScores.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.yambScores_data = {'player1_name': 'Milan', 'player1_score': 500, 'player2_name': 'Emma', 'player2_score': 600}
        self.response = self.client.post(
                reverse('create'),
                self.yambScores_data,
                format="json")

    def test_api_can_create_a_yamb_score(self):
        """Test the api has yamb score creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_yamb_score(self):
        """Test the api has yamb score retrieval capability."""
        yamb_score = YambScores.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': yamb_score.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, yamb_score)

    def test_api_can_update_yamb_score(self):
        """Test the api can update a given yamb score."""
        yamb_score = YambScores.objects.get()
        change_yamb_score = {'player1_name': 'Milan', 'player1_score': 800, 'player2_name': 'Emma', 'player2_score': 600}
        response = self.client.put(
            reverse('details', kwargs={'pk': yamb_score.id}),
            change_yamb_score, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_yamb_score(self):
        """Test the api can delete a yamb score."""
        yamb_score = YambScores.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': yamb_score.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)