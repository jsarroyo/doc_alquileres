# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class Edificio(models.Model):
    _name = 'Alquileres.Edificio'

    id = fields.Integer()
    nombre = fields.Char("Nombre del Edificio")
    direccion = fields.Char("Direccion del Edificio")
    area_terreno  = fields.Float()
    area_construida  = fields.Float()
    valor_real   = fields.Float()
    valor_fiscal  = fields.Float()
    lista_pisos = fields.One2many("Alquileres.Piso", "piso_id", string="Pisos")
    #order_count = fields.Integer(compute='_get_total_sold',
    #                             store=True,
    #                             string="Total sold")
    


    # @api.depends('order_ids')
    # def _get_total_sold(self):
    #     for plant in self:
    #         plant.order_count = len(plant.order_ids)

    # @api.constrains('order_count', 'number_in_stock')
    # def _check_available_in_stock(self):
    #     for plant in self:
    #         if plant.number_in_stock and \
    #           plant.order_count > plant.number_in_stock:
    #             raise UserError("There is only %s %s in stock but %s were sold"
    #                   % (plant.number_in_stock, plant.name, plant.order_count))
