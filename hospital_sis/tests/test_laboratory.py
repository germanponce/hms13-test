# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestLaboratory(common.TransactionCase):

    def setUp(self):
        super(TestLaboratory, self).setUp()
        # 'sis.laboratory' instance model
        self.laboratory = self.env['sis.laboratory']

        # create an 'laboratory' record
        self.laboratory1 = self.laboratory.create({
            'name': 'Hematology',
            'user_id': self.env.ref('base.user_admin').id,
            'hospital_id': self.env.ref('hospital_sis.hospital1').id,
        })

        self.laboratory2 = self.laboratory.create({
            'name': 'Echocardiography',
            'user_id': self.env.ref('base.user_root').id,
            'hospital_id': self.env.ref('hospital_sis.hospital1').id,
        })

    def test_laboratorys_creation(self):
        # This function test the 'sis.laboratory' instances creation functionality

        # check 'name' of the 'laboratory1'
        self.assertEqual(self.laboratory1.name, 'Hematology')
        _logger.info("Created the {0}'s Laboratory at {1}!".format(
            self.laboratory1.name,
            self.env.ref('hospital_sis.hospital1').name)
        )

        # check 'name' of the 'laboratory2'
        self.assertEqual(self.laboratory2.name, 'Echocardiography')
        _logger.info("Created the {0}'s Laboratory at {1}!".format(
            self.laboratory2.name,
            self.env.ref('hospital_sis.hospital1').name)
        )

        _logger.info("Your 'TestLaboratory' test was successful!")
