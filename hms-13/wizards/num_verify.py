# -*- coding: utf-8 -*-
import requests
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class NumVerify(models.TransientModel):
    _name = 'num.verify'

    patient = fields.Many2one('hospital.patient', string="Patient")
    mobile = fields.Char(string="Mobile", related='patient.mobile')

    # country_id = fields.Many2one('res.country', related='patient.country_id', string="Country")

    def verify_phone(self):
        for rec in self:
            vals = {
                'patient': rec.patient.id,
                'mobile': rec.patient.mobile,
                'access_key': rec.env['ir.config_parameter'].search([('key', '=', 'access_key')]).value if rec.env[
                    'ir.config_parameter'].search([('key', '=', 'access_key')]) else '',
                'url': rec.env['ir.config_parameter'].search([('key', '=', 'num_verify_url')]).value if rec.env[
                    'ir.config_parameter'].search([('key', '=', 'num_verify_url')]) else '',
                'country_code': rec.patient.country_id.code,
            }
            country_code = vals.get('country_code')
            access_key = vals.get('access_key')
            mobile = vals.get('mobile')
            url = vals.get('url')
            if access_key and mobile:
                url = url % (access_key, mobile, country_code)
            print(vals)
            print(access_key)
            print(url)

            response = requests.get(url).json()
            print(response)
            if response and response.get('valid') == True:
                return vals




    # @api.constrains('country_id', 'phone')
    # def _check_country_vs_phone(self):
    #     for rec in self:
    #         if rec.country_id and rec.phone:
    #             # Get the country's code for the country that the user has entered
    #             country_code = rec.country_id.code
    #
    #             # Check if the VerifyNum is enabled
    #
    #             params = rec.env['ir.config_parameter'].sudo()
    #             enable_verifynum = params.get_param('enable_verifynum')
    #             verifynum_api_key = params.get_param('verifynum_api_key', default='')
    #
    #             if enable_verifynum and verifynum_api_key:
    #                 url = 'http://apilayer.net/api/validate?access_key=%s&number=%s&format=1' % (
    #                     verifynum_api_key, rec.phone)
    #                 response = requests.get(url).json()
    #                 # Raise the errors if something was not valid.
    #                 if 'valid' in response.keys() and response.get('valid') and not response.get(
    #                         'country_code') == country_code:
    #                     raise UserError(_('The country is not matching the phone number'))
    #                 elif 'valid' in response.keys() and not response.get('valid'):
    #                     raise UserError(_('Phone Number is not correct'))
    #             elif enable_verifynum and not verifynum_api_key:
    #                 raise UserError(_('NumVerify is enabled but the Access Key is not configured!'))
    #             else:
    #                 pass
    #
    # @api.constrains('country_id', 'mobile')
    # def _check_country_vs_mobile(self):
    #     for rec in self:
    #         if rec.country_id and rec.mobile:
    #             # Get the country's code for the country that the user has entered
    #             country_code = rec.country_id.code
    #
    #             # Check if the VerifyNum is enabled
    #
    #             params = rec.env['ir.config_parameter'].sudo()
    #             enable_verifynum = params.get_param('enable_verifynum')
    #             verifynum_api_key = params.get_param('verifynum_api_key', default='')
    #
    #             if enable_verifynum and verifynum_api_key:
    #                 url = 'http://apilayer.net/api/validate?access_key=%s&number=%s&format=1' % (
    #                     verifynum_api_key, rec.mobile)
    #                 response = requests.get(url).json()
    #                 # Raise the errors if something was not valid.
    #                 if 'valid' in response.keys() and response.get('valid') and not response.get(
    #                         'country_code') == country_code:
    #                     raise UserError(_('The country is not matching the mobile number'))
    #                 elif 'valid' in response.keys() and not response.get('valid'):
    #                     raise UserError(_('Mobile Number is not correct'))
    #             elif enable_verifynum and not verifynum_api_key:
    #                 raise UserError(_('NumVerify is enabled but the Access Key is not configured!'))
    #             else:
    #                 pass
