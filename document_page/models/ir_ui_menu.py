# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0) 
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################

from odoo import models


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    def _visible_menu_ids(self, debug=False):
        visible_ids = super()._visible_menu_ids(debug)
        if self._context.get("ir.ui.menu.authorized_list"):
            # Add the authorized by groups menus that does not have an action
            menus = (
                self.with_context(**{"ir.ui.menu.full_list": True}).search([]).sudo()
            )
            groups = (
                self.env.user.groups_id
                if not debug
                else self.env.user.groups_id - self.env.ref("base.group_no_one")
            )
            authorized_menus = menus.filtered(
                lambda m: not m.groups_id or m.groups_id and groups
            )
            authorized_folder_menus = authorized_menus.filtered(lambda m: not m.action)
            visible_ids = visible_ids.union(authorized_folder_menus.ids)
        return visible_ids
