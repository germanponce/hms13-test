# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestConsultation(common.TransactionCase):

    def setUp(self):
        super(TestConsultation, self).setUp()
        # 'sis.consultation' instance model
        self.consultation = self.env['sis.consultation']

        # create an 'consultation' record
        self.consultation1 = self.consultation.create({
            'name': 'Hematology',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'specialty': self.env.ref('hospital_sis.specialty2').id,
        })

        self.consultation2 = self.consultation.create({
            'name': 'Echocardiography',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'specialty': self.env.ref('hospital_sis.specialty3').id,
        })

    def test_consultations_creation(self):
        # This function test the 'sis.consultation' instances creation functionality

        # check 'name' of the 'consultation1'
        self.assertEqual(self.consultation1.name, 'Hematology')
        _logger.info("Created the {0}'s Consultation at {1}!".format(
            self.consultation1.name,
            self.env.ref('hospital_sis.hospital1').name)
        )

        # check 'name' of the 'consultation2'
        self.assertEqual(self.consultation2.name, 'Echocardiography')
        _logger.info("Created the {0}'s Consultation at {1}!".format(
            self.consultation2.name,
            self.env.ref('hospital_sis.hospital1').name)
        )

        _logger.info("Your 'TestConsultation' test was successful!")
