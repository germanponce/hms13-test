# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestHospital(common.TransactionCase):

    def setUp(self):
        super(TestHospital, self).setUp()
        # 'sis.hospital' instance model
        self.hospital = self.env['sis.hospital']

        # create an 'hospital' record
        self.hospital1 = self.hospital.create({
            'name': 'Sor Juana Ines de la Cruz',
            'country_id': self.env.ref('base.cl').id,
        })

        self.hospital2 = self.hospital.create({
            'name': 'Hospital Universitario de Los Andes',
            'country_id': self.env.ref('base.cl').id,
        })

    def test_hospitals_creation(self):
        # This function test the 'sis.hospital' instances creation functionality

        # check 'name' of the 'hospital1'
        self.assertEqual(self.hospital1.name, 'Sor Juana Ines de la Cruz')
        _logger.info("Created the {0}'s Hospital!".format(self.hospital1.name))

        # check 'name' of the 'hospital2'
        self.assertEqual(self.hospital2.name, 'Hospital Universitario de Los Andes')
        _logger.info("Created the {0}'s Hospital!".format(self.hospital2.name))

        _logger.info("Your 'TestHospital' test was successful!")
