# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Laboratory(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'sis.laboratory'
    # field to use for labeling records
    _rec_name = 'name'
    # the model's informal name
    _description = 'Hospital Laboratories'

    name = fields.Char(string="Laboratory Name", required=True)
    user_id = fields.Many2one(comodel_name="res.users", string="Responsible", required=True)
    hospital_id = fields.Many2one(comodel_name="sis.hospital", string="Hospital", required=True)
