from django.test import TestCase
from things.models import Thing
from things.forms import ThingForm

class formTest(TestCase):
    def setUp(self):
        self.form_input ={
            'name': 'Jane',
            'description': 'fjsdfklsdjflsdjf',
            'quantity' : 2,
        }
    
    def test_valid_input_data(self):
        form = ThingForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    def test_quantity_cant_be_negative(self):
        self.form_input["quantity"] = -1
        form = ThingForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_name_cant_be_36_chars_long(self):
        self.form_input["name"] = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        form = ThingForm(data = self.form_input)
        self.assertFalse(form.is_valid())