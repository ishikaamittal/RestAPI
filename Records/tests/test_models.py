from django.test import TestCase
from ..models import Records


class RecordTest(TestCase):
    """ Test module for Record model """

    def setUp(self):
        Records.objects.create(
            name='Guppy', species='xyz',weight=12, height=13,file='guppy.jpg',latitude=12, longitude=14)
        Records.objects.create(
           name='muppy', species='abc',weight=12, height=13,file='muppy.jpg',latitude=12, longitude=14)

    def test_Species(self):
        record_guppy = Records.objects.get(name='Guppy')
        record_muppy = Records.objects.get(name='muppy')
        self.assertEqual(
            record_guppy.get_species(), "Guppy belongs to xyz species.")
        self.assertEqual(
            record_muppy.get_species(), "Muppy belongs to abc breed.") #this will fail because of name error muppy != Muppy