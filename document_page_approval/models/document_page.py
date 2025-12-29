# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################
# Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import UserError

class DocumentPage(models.Model):
    _inherit = "document.page"

    approval_state = fields.Selection(
        [
            ("draft", "Draft"),
            ("waiting", "Waiting for Approval"),
            ("approved", "Approved"),
        ],
        default="draft",
        tracking=True,
    )

    def action_request_approval(self):
        for page in self:
            page.approval_state = "waiting"

    def action_approve(self):
        for page in self:
            page.approval_state = "approved"

    def action_reset_to_draft(self):
        for page in self:
            page.approval_state = "draft"

    @api.onchange("approval_state")
    def _onchange_approval_state(self):
        if self.approval_state == "approved" and not self.content:
            raise UserError(
                self.env._("You cannot approve a document without content.")
            )