# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

# Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DocumentPageHistory(models.Model):
    _name = "document.page.history"
    _description = "Document Page History"
    _order = "create_date desc, id desc"

    name = fields.Char(translate=True)
    page_id = fields.Many2one("document.page", required=True, ondelete="cascade")
    content = fields.Html()
    create_date = fields.Datetime(readonly=True)
    create_uid = fields.Many2one("res.users", readonly=True)