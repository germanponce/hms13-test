# -*- coding: utf-8 -*-

import datetime, dateutil
import re

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Appointment Booking"
    _rec_name = 'patient'

    name = fields.Char(string="Appointment", readonly=True, required=True, copy=False, default='New')
    appointment_date = fields.Datetime(string="Appointment Date", required=True, copy=False)
    appointment_status = fields.Selection([('a', 'New'),
                                           ('b', 'Accepted'),
                                           ('c', 'Rejected')], string="Status", default='a', readonly=True, copy=False)
    patient = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor = fields.Many2one('hospital.doctor', string="Doctor")
    consultation_notes = fields.Text(string="Notes")
    prescription = fields.Text(string="Medicines")
    state = fields.Selection([
        ('draft', "Draft"),
        ('confirm', "Confirm"),
        ('done', "Done"),
        ('cancel', "Cancelled"),
    ], string="Status", readonly=True, default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or 'New'
        result = super(Appointment, self).create(vals)
        return result

    @api.onchange('appointment_date')
    def _onchange_appointment_date(self):
        if self.appointment_date:
            if self.appointment_date < datetime.datetime.today():
                raise ValidationError("Please enter a future date.")

    def accept_appointment(self):
        views = [(self.env.ref('hospital.appointment_tree_view').id, 'tree'),
                 (self.env.ref('hospital.view_appointment_form').id, 'form')]
        return {
            'name': 'Appointments',
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'view_id': False,
            'res_model': 'hospital.appointment',
            'views': views,
            'domain': [('id', 'in', self.id)],
            'type': 'ir.actions.act_window',
            'context': {'patient': self.patient, 'appointment_date': self.appointment_date}
        }

    def action_confirm(self):
        for rec in self:
            if rec.appointment_status == 'b':
                rec.state = 'confirm'
            else:
                rec.state = 'cancel'

    def action_done(self):
        for rec in self:
            if rec.appointment_status == 'b':
                rec.state = 'done'
            else:
                rec.state = 'cancel'
                raise ValidationError("This appointment is rejected")

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_accept(self):
        for rec in self:
            if rec.appointment_status == 'a':
                rec.appointment_status = 'b'
            elif rec.appointment_status == 'b':
                raise ValidationError("Already accepted.")
            else:
                raise ValidationError("This appointment cannot be accepted!")

    def action_reject(self):
        for rec in self:
            if rec.appointment_status == 'a':
                rec.appointment_status = 'c'
            elif rec.appointment_status == 'b':
                raise ValidationError("Already accepted.")
            else:
                raise ValidationError("Already Rejected.")

