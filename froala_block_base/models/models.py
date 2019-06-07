# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class froala_block_testimonials(models.Model):
#     _name = 'froala_block_testimonials.froala_block_testimonials'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100