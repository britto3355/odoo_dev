# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], string="status")
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals["note"] = 'New Patient'
            res = super(HospitalPatient, self).create(vals)
            return res

        @api.onchange('partner_id')
        def onchange_partner_id(self):
            if self.patient_id:
                if self.patient_id.gender:
                    self.gender = self.patient_id.gender
                else:
                    self.gender = ''
