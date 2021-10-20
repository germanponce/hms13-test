# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import AccessDenied


class ResConfigSettings(models.TransientModel):
    _name = 'custom.config.parameter'
    _inherit = 'ir.config_parameter'

    access_key = fields.Char("VerifyNum Api Key")
    num_verify_url = fields.Char("VerifyNum URL")
