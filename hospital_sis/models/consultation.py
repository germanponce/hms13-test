# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Consultation(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'sis.consultation'
    # field to use for labeling records
    _rec_name = 'name'
    # the model's informal name
    _description = 'Hospital Consultations'

    name = fields.Char(string="Name", size=80, requerid=True, help='Enter the name')
    partner_id = fields.Many2one(comodel_name="res.partner", string="Patient",
                                 ondelete='restrict', requerid=False)
    specialty = fields.Many2one(comodel_name="sis.specialty", string="Specialty",
                                ondelete='restrict', requerid=False)
