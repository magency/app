#-*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Comment

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class CommentTest(TestCase):
    def test_is_recent_with_future_comment(self):
        """
        vérifie si la méthode is_recent d'un Article ne
        renvoie pas True si l'Article a sa date de publication
        dans le futur.
        """
        future_comment = Comment(date=datetime.now() + timedelta(days=20))
        self.assertEqual(future_comment.is_recent(), False)