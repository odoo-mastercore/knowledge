# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0)
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################


{
    "name": "Document Page Approval",
    "version": "19.0.1.0.0",
    "author": "Mastercore Sinapsys Global®",
    "website": "https://www.mastercore.co",
    "license": "OPL-1",
    "category": "Knowledge Management",
    "summary": "Request and track approvals for document page changes.",
    "description": "Adds approval workflow and notifications for document pages.",
    "depends": ["document_page", "mail"],
    "data": [
        "data/email_template.xml",
        "views/document_page_approval.xml",
        "security/document_page_security.xml",
    ],
    "images": [
        "images/category.png",
        "images/page_history_list.png",
        "images/page_history.png",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "installable": True,
}
