"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch

from decimal import Decimal

from core import models


def create_sample_user(email='user@example.com', password='testpass123'):
    """ Create and return a sample user """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """ Test Models"""

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')

            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raise_error(self):
        """ Test creating user without email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'sample123')

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """ Test creating a new recipe is successful """
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample Recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """ Test creating a new tag is successful """
        user = create_sample_user()
        tag = models.Tag.objects.create(user=user, name='Vegan')

        self.assertEqual(str(tag), tag.name)

    def test_create_ingridient(self):
        """ Test creating an ingridient is successful """
        user = create_sample_user()
        ingridient = models.Ingredient.objects.create(
            user=user,
            name='Cucumber'
        )

        self.assertEqual(str(ingridient), ingridient.name)

    @patch('core.models.uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """ Test generating image path """
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        expected_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, expected_path)
