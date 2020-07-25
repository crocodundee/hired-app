from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def base_skill(name="Skill"):
    """Create sample skill object"""
    return models.Skill.objects.create(name=name)


class TestModels(TestCase):
    """Test app models"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )

    def test_create_skill_success(self):
        """Test skill object creation"""
        skill = models.Skill.objects.create(name="Python", level=models.Skill.ADVANCED)

        self.assertEqual(str(skill), skill.name)

    def test_create_resume_success(self):
        """Test user can create base resume"""
        skill_1 = base_skill("Python")
        skill_2 = base_skill("Django")

        resume = models.Resume.objects.create(
            user=self.user,
            position="Junior Python Developer",
            summury="Responsive, professional person",
        )

        resume.skills.add(skill_1)
        resume.skills.add(skill_2)

        expected = (
            f"{resume.user.first_name} {resume.user.last_name} - {resume.position}"
        )

        self.assertEqual(str(resume), expected)
        self.assertEqual(resume.skills.count(), 2)
