# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

{
    "name": "Document Page Approval",
    "summary": "Approval workflow for document pages.",
    "description": """
Adds an approval workflow to document pages.
Allows controlling publication of knowledge pages through approval states
and access rules based on user groups.
    """,
    "version": "19.0.1.0.0",
    "category": "Knowledge Management",
    "author": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/knowledge",
    "license": "AGPL-3",
    "depends": [
        "document_page",
    ],
    "data": [
        "security/document_page_approval_security.xml",
        "views/document_page_approval.xml",
    ],
    "installable": True,
}