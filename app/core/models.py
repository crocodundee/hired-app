from django.db import models
from django.contrib.auth import get_user_model


class Resume(models.Model):
    """Basic resume for job applicant"""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    position = models.CharField(max_length=255, blank=False)
    summury = models.TextField(blank=False)

    def __str__(self):
        """String represent of model"""
        return f"{self.user.first_name} {self.user.last_name} - {self.position}"
