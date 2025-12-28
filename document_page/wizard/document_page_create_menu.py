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


class DocumentPageCreateMenu(models.TransientModel):
    """Create Menu."""

    _name = "document.page.create.menu"
    _description = "Wizard Create Menu"

    menu_name = fields.Char(required=True)
    menu_parent_id = fields.Many2one("ir.ui.menu", string="Parent Menu")
    page_id = fields.Many2one("document.page", string="Page", required=True)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if self.env.context.get("active_model") == "document.page" and self.env.context.get(
            "active_id"
        ):
            res["page_id"] = self.env.context["active_id"]
            res["menu_name"] = self.env["document.page"].browse(res["page_id"]).name
        return res

    def create_menu(self):
        self.ensure_one()
        menu = self.env["ir.ui.menu"].create(
            {
                "name": self.menu_name,
                "parent_id": self.menu_parent_id.id or False,
            }
        )
        self.page_id.menu_id = menu
        return {"type": "ir.actions.act_window_close"}