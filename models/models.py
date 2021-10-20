# -*- coding: utf-8 -*-
from odoo import models, fields


class Hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    name = fields.Char(string="Hospital Name")
    doctor = fields.Many2one('hospital.doctor', string="Doctor")
    patient = fields.Many2one('hospital.patient', string="Patient")


