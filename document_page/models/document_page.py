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
from odoo.exceptions import ValidationError


class DocumentPage(models.Model):
    """This class is use to manage Document."""

    _name = "document.page"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Document Page"
    _parent_name = "parent_id"
    _order = "sequence, name"

    name = fields.Char(required=True, translate=True)
    content = fields.Html(
        compute="_compute_content",
        inverse="_inverse_content",
        search="_search_content",
        sanitize_style=True,
    )
    content_unsafe = fields.Html()
    draft = fields.Boolean(default=True)
    history_id = fields.Many2one("document.page.history", readonly=True)
    history_ids = fields.One2many(
        "document.page.history",
        "page_id",
        string="History",
        readonly=True,
    )
    history_head = fields.Many2one(
        "document.page.history",
        "HEAD",
        compute="_compute_history_head",
        store=True,
        auto_join=True,
    )
    create_date = fields.Datetime(readonly=True)
    write_date = fields.Datetime(readonly=True)
    create_uid = fields.Many2one("res.users", readonly=True)
    write_uid = fields.Many2one("res.users", readonly=True)

    # Hierarchy
    parent_id = fields.Many2one("document.page", string="Category")
    child_ids = fields.One2many("document.page", "parent_id", string="Children")
    menu_id = fields.Many2one("ir.ui.menu", string="Menu")
    sequence = fields.Integer(default=10)

    # Misc
    backend_url = fields.Char(compute="_compute_backend_url", string="Backend URL")

    content_uid = fields.Many2one(
        "res.users",
        "Last Contributor",
        related="history_head.create_uid",
        store=True,
        index=True,
        readonly=True,
    )
    company_id = fields.Many2one(
        "res.company",
        "Company",
        help="If set, page is accessible only from this company",
        index=True,
        ondelete="cascade",
        default=lambda self: self.env.company,
    )
    
    image = fields.Binary(attachment=True)
    color = fields.Integer(string="Color Index")

    def _compute_backend_url(self):
        tmpl = "/web#id={}&model=document.page&view_type=form"
        for rec in self:
            url = tmpl.format(rec.id)
            # retrieve action
            action = None
            parent = rec
            while not action and parent:
                action = parent.menu_id.action
                parent = parent.parent_id
            if action:
                url += f"&action={action.id}"
            rec.backend_url = url

    @api.constrains("parent_id")
    def _check_parent_id(self):
        if self._has_cycle():
            raise ValidationError(self.env._("You cannot create recursive categories."))

    def _get_page_index(self, link=True):
        self.ensure_one()
        names = []
        parent = self
        while parent:
            if link:
                names.append(
                    f'<a href="#" data-oe-model="{parent._name}" data-oe-id="{parent.id}">{parent.display_name}</a>'
                )
            else:
                names.append(parent.display_name)
            parent = parent.parent_id
        return " / ".join(reversed(names))

    def _compute_content(self):
        for page in self:
            if page.content_unsafe:
                page.content = page.content_unsafe
            else:
                page.content = False

    def _inverse_content(self):
        for page in self:
            page.content_unsafe = page.content
            page._create_history(page.content)

    def _create_history(self, content):
        self.ensure_one()
        vals = {
            "page_id": self.id,
            "name": self.name,
            "content": content,
        }
        history = self.env["document.page.history"].create(vals)
        self.history_id = history

    def _search_content(self, operator, value):
        return [("content_unsafe", operator, value)]

    @api.depends("history_ids")
    def _compute_history_head(self):
        for rec in self:
            if rec.history_ids:
                rec.history_head = rec.history_ids[0]
            else:
                rec.history_head = False

    @api.onchange("parent_id")
    def _onchange_parent_id(self):
        for rec in self:
            if rec.parent_id and rec.menu_id and not rec.parent_id.menu_id:
                rec.parent_id.menu_id = rec.menu_id

    def unlink(self):
        for page in self:
            page.history_ids.unlink()
        return super().unlink()

    def copy(self, default=None):
        default = dict(default or {})
        default.setdefault("name", self.env._("%s (copy)") % self.name)
        default.setdefault("history_id", False)
        default.setdefault("history_ids", False)
        return super().copy(default=default)