# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0)
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################


from odoo import fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    # Add index to res_model because filtering on it is a common use case
    res_model = fields.Char(index=True)
