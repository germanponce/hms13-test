# -*- coding: utf-8 -*-

import datetime, dateutil
import re

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'hospital Doctor'
    _rec_name = 'name'

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('doctor', '=', self.id)])
        self.appointment_count = count

    name = fields.Char(string="Name", required=True)
    gender = fields.Selection([('m', "Male"),
                               ('f', "Female"),
                               ('o', "Other")])
    birthdate = fields.Date(string="Birth Date")
    age = fields.Float(string="Age", compute='_compute_age')
    mobile = fields.Char(string="Mobile No")
    address = fields.Text(string="Address")
    appointment_count = fields.Integer(string="Appointment", compute='get_appointment_count')

    @api.onchange('birthdate')
    def _onchange_birthdate(self):
        if self.birthdate:
            if self.birthdate >= datetime.date.today():
                msg = "Future date is not allowed!"
                raise ValidationError(msg)

    @api.onchange('mobile')
    def _onchange_phone(self):
        if self.mobile:
            pattern = re.compile(r'(?:0|\+?91)\s?(?:\d\s?){9,11}$')
            if not pattern.match(self.mobile):
                raise ValidationError("Invalid mobile number.")

    @api.depends('birthdate')
    def _compute_age(self):
        if self.birthdate:
            today = datetime.date.today()
            offset = int(self.birthdate.replace(year=today.year) > today)
            self.age = datetime.date.today().year - self.birthdate.year - offset
        else:
            self.age = 0.0

    def open_doctor_appointments(self):
        return {
            'name': 'Appointmetnts',
            'domain': [('doctor', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

