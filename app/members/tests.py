# tests.py

from django.test import TestCase
from .models import Member

class MemberModelTestCase(TestCase):

    def test_member_creation(self):
        member = Member.objects.create(
            Topic="Test Topic",
            Description="Test Description",
            by="Test Author",
            date="2023-01-01"  # Make sure to provide a valid date format
        )

        self.assertEqual(member.Topic, "Test Topic")
        self.assertEqual(member.Description, "Test Description")
        self.assertEqual(member.by, "Test Author")
        self.assertEqual(member.date, "2023-01-01")  # Update with the actual expected date format
