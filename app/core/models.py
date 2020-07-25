from django.contrib.auth import get_user_model
from django.db import models


class Skill(models.Model):
    """Applicant skill item"""

    BEGGINER, MIDDLE, ADVANCED = 0, 1, 2
    SKILL_LEVELS = ((BEGGINER, "Begginer"), (MIDDLE, "Middle"), (ADVANCED, "Advanced"))

    name = models.CharField(max_length=255, blank=False)
    level = models.CharField(max_length=8, choices=SKILL_LEVELS, blank=True)

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
