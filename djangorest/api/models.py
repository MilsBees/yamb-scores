from django.db import models

class YambScores(models.Model):
    """This class represents the yamb scores model."""
    player1_name = models.CharField(max_length=255, blank=False)
    player1_score = models.SmallIntegerField()
    player2_name = models.CharField(max_length=255, blank=False)
    player2_score = models.SmallIntegerField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = "Yamb Scores"