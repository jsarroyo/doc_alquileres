# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class piso(models.Model):
    _name = 'doc_alquileres.pisos'

    id = fields.Integer() 
    edificio_id = fields.Integer()