# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class Local(models.Model):
    _name = 'doc_alquileres.Local'
    id = fields.Integer()
    area_M2 = fields.Float()
    medidor_electrico  = fields.Char()
    medidor_agua = fields.Char()
    piso_id = fields.Integer()
    edificio_id = fields.Integer()