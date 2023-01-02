from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Score(models.Model):
    score = models.IntegerField()
    name = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Game(models.Model):
    """This class represents the yamb scores model."""
    player1_name = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player1_name")
    player1_score = models.ManyToManyField(Score, blank=False, related_name="player1_score")
    player2_name = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player2_name")
    player2_score = models.ManyToManyField(Score, blank=False, related_name="player2_score")

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.id