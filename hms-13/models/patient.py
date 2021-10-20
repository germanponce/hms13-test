# -*- coding: utf-8 -*-
import requests

from odoo import fields, models, api
from odoo.exceptions import ValidationError
import datetime


class Patient(models.Model):
    _name = 'hospital.patient'

    @api.model
    def create(self, vals_list):
        res = super(Patient, self).create(vals_list)
        return res

    # Add a new column to the res.partner model, by default partners are not
    patient = fields.Many2many('res.partner', string="Patient")
    name = fields.Char(string="Name", required=True)
    birthdate = fields.Date(string="Birth Date")
    age = fields.Float(string="Age", compute='_compute_age', default=0.0)
    gender = fields.Selection([('m', "Male"),
                               ('f', "Female"),
                               ('o', "Other")])
    mobile = fields.Char(string="Mobile No")
    country_id = fields.Many2one('res.country', string="Country")
    verification = fields.Boolean(string="Verification Status", defualt=False, readonly=True)

    @api.onchange('birthdate')
    def _onchange_birthdate(self):
        if self.birthdate:
            if self.birthdate >= datetime.date.today():
                msg = "Future date is not allowed!"
                raise ValidationError(msg)

    @api.depends('birthdate')
    def _compute_age(self):
        if self.birthdate:
            today = datetime.date.today()
            offset = int(self.birthdate.replace(year=today.year) > today)
            self.age = datetime.date.today().year - self.birthdate.year - offset
        else:
            self.age = 0.0

    def verify_num(self):
        if self.mobile and self.country_id and self.verification == False:
            for rec in self:
                vals = {
                    'mobile': rec.mobile,
                    'access_key': rec.env['ir.config_parameter'].search([('key', '=', 'access_key')]).value if rec.env[
                        'ir.config_parameter'].search([('key', '=', 'access_key')]) else '',
                    'url': rec.env['ir.config_parameter'].search([('key', '=', 'num_verify_url')]).value if rec.env[
                        'ir.config_parameter'].search([('key', '=', 'num_verify_url')]) else '',
                    'country_code': rec.country_id.code,
                }
                country_code = vals.get('country_code')
                access_key = vals.get('access_key')
                mobile = vals.get('mobile')
                url = vals.get('url')
                if access_key and mobile:
                    url = url % (access_key, mobile, country_code)
                print(access_key)
                print(url)
                print(country_code)
                response = requests.get(url).json()
                print(response)
                if response and response.get('valid') == True:
                    if rec.verification != 'verified':
                        rec.verification = True
                    else:
                        raise ValidationError("Already verified.")
                else:
                    rec.verification = False
                    raise ValidationError("Verification failed!")
