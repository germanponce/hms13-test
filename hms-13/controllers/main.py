from odoo import http
from odoo.http import request


class Hospital(http.Controller):

    @http.route('/hospital/patient/', website=True, auth='public')
    def hospital_patient(self, **kw):

        keys = request.env['ir.config_parameter'].sudo().search([('key', '=', 'access_key')])
        print("keys....", keys)
        return request.render("hospital.patient_page", {
            'keys': keys
        })