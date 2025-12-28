# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

# Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class DocumentPageShowDiff(models.TransientModel):
    _name = "document.page.show.diff"
    _description = "Wizard Show Diff"

    page_id = fields.Many2one("document.page", required=True)
    history_id_1 = fields.Many2one("document.page.history", required=True)
    history_id_2 = fields.Many2one("document.page.history", required=True)
    diff = fields.Html(readonly=True)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if self.env.context.get("active_model") == "document.page" and self.env.context.get(
            "active_id"
        ):
            res["page_id"] = self.env.context["active_id"]
        return res