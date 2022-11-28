from django.db import models

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    # player1_name = models.CharField(max_length=255, blank=False)
    # player1_score = models.SmallIntegerField()
    # player2_name = models.CharField(max_length=255, blank=False)
    # player2_score = models.SmallIntegerField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
