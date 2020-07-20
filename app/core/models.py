from django.db import models
from django.contrib.auth import get_user_model


class Skill(models.Model):
    """Applicant skill item"""

    name = models.CharField(max_length=255, blank=False)
    level = models.PositiveSmallIntegerField(max_value=10, blank=False)

    def __str__(self):
        """String representing of skill model"""
        return self.name


class Resume(models.Model):
    """Basic resume for job applicant"""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    position = models.CharField(max_length=255, blank=False)
    summury = models.TextField(blank=False)
    skills = models.ManyToManyField(to="Skill")

    def __str__(self):
        """String represent of model"""
        return f"{self.user.first_name} {self.user.last_name} - {self.position}"
