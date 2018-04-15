# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class Local(models.Model):
    _name = 'Alquileres.Local'

    numero  = fields.Integer() 
    area_M2 = fields.Float()
	numero_medidor_electrico = fields.Char("# Medidor de electricidad")
	numero_medidor_agua = fields.Char("#Medidor de acueducto")
	piso_id = fields.Integer()
	edificio_id = fields.Integer()