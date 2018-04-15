# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class Piso(models.Model):
    _name = 'Alquileres.Piso'

    numero = fields.Integer() 
    edificio_id = fields.Integer()