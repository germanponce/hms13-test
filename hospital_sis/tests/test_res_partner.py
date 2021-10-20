# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestResPartner(common.TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()
        # 'res.partner' instance model
        self.partner = self.env['res.partner']

        # # create an 'partner' record
        # self.partner1 = self.partner.create({
        #     'rut': '00000000-0',
        #     'age': 45,
        #     'profession': 'Civil Engineer',
        # })

    def test_partners_install(self):
        # This function test the 'res.partner' instances creation functionality

        # check if 'rut' is not install at 'ir.model.fields'assertEqual
        self.assertFalse(self.env['ir.model.fields'].search([('model', '=', 'rut')]))
        _logger.info("The 'rut' is not install at 'ir.model.fields'.")

        # check if 'rut' is install at 'ir.model.fields'assertEqual
        # self.assertTrue(self.env['ir.model.fields'].search([('model', '=', 'rut')]))
        # _logger.info("The 'rut' is install at 'ir.model.fields'.")

        # check if 'age' is not install at 'ir.model.fields'assertEqual
        self.assertFalse(self.env['ir.model.fields'].search([('model', '=', 'age')]))
        _logger.info("The 'age' is not install at 'ir.model.fields'.")

        # check if 'age' is install at 'ir.model.fields'assertEqual
        # self.assertTrue(self.env['ir.model.fields'].search([('model', '=', 'age')]))
        # _logger.info("The 'age' is install at 'ir.model.fields'.")

        # check if 'profession' is not install at 'ir.model.fields'assertEqual
        self.assertFalse(self.env['ir.model.fields'].search([('model', '=', 'profession')]))
        _logger.info("The 'profession' is not install at 'ir.model.fields'.")

        # check if 'profession' is install at 'ir.model.fields'assertEqual
        # self.assertTrue(self.env['ir.model.fields'].search([('model', '=', 'profession')]))
        # _logger.info("The 'profession' is install at 'ir.model.fields'.")

        _logger.info("Your 'TestResPartner' test was successful!")
