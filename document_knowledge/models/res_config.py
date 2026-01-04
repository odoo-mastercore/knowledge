# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0)
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################


from odoo import fields, models


class DocumentKnowledgeConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_ir_attachment_user = fields.Boolean(
        string="Central access to Documents",
        implied_group="document_knowledge.group_ir_attachment_user",
    )
