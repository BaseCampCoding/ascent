from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from . import models

# Create your tests here.
class TestStudentCreatesInitiative(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")

        self.client.force_login(user)

        self.client.post(
            reverse("initiatives:create"),
            {"title": "recycling", "description": "reduce! reuse! recycle!"},
        )

        self.assertEqual(user.initiative_set.count(), 1)

        initiative = user.initiative_set.first()

        self.assertEqual(initiative.title, "recycling")
        self.assertEqual(initiative.description, "reduce! reuse! recycle!")

    def test_with_no_data(self):
        user = User.objects.create_user("selfstartersuz")

        self.client.force_login(user)

        response = self.client.post(reverse("initiatives:create"))

        self.assertEqual(user.initiative_set.count(), 0)

        self.assertContains(response, "is required")


class TestUserSeesInitiatives(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")
        user.initiative_set.create(title="BLOAW", description="Doing big things!")

        response = self.client.get(reverse("initiatives:home"))

        self.assertContains(response, "BLOAW")