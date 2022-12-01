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
