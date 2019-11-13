from django.test import TestCase
from model_mommy import mommy
from catalog.models import Category, Product

class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = mommy.make('catalog.Category')
        