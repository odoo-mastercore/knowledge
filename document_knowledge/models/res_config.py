# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

from odoo import fields, models


class DocumentKnowledgeConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_ir_attachment_user = fields.Boolean(
        string="Central access to Documents",
        implied_group="document_knowledge.group_ir_attachment_user",
    )