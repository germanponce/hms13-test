# Do a little print to show it visually for this demo - in production you don't really need this.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestSpecialty(common.TransactionCase):

    def setUp(self):
        super(TestSpecialty, self).setUp()
        # 'sis.specialty' instance model
        self.specialty = self.env['sis.specialty']

        # create an 'specialty' record
        self.specialty1 = self.specialty.create({
            'name': 'Angiology',
        })

        self.specialty2 = self.specialty.create({
            'name': 'Cardiology',
        })

    def test_specialties_creation(self):
        # This function test the 'sis.specialty' instances creation functionality

        # check 'name' of the 'specialty1'
        self.assertEqual(self.specialty1.name, 'Angiology')
        _logger.info("Created the {0}'s Specialty!".format(self.specialty1.name))

        # check 'name' of the 'specialty2'
        self.assertEqual(self.specialty2.name, 'Cardiology')
        _logger.info("Created the {0}'s Specialty!".format(self.specialty2.name))

        _logger.info("Your 'TestSpecialty' test was successful!")
