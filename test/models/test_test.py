# -*- coding: utf-8 -*-
# Copyright (C) 2019 - Teclib'ERP (<https://www.teclib-erp.com>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning
import logging

_logger = logging.getLogger(__name__)

class TestTest(models.Model):
    _name = "test.test"
    
    _description = "Test Test"
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    
