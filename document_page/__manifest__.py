# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0) 
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################


{
    "name": "Document Page",
    "version": "19.0.1.0.4",
    "category": "Knowledge Management",
    "summary": "Manage internal wiki-style document pages.",
    "description": "Knowledge base pages with history tracking and menu integration.",
    "author": "Mastercore Sinapsys Global®",
    "website": "https://www.mastercore.co",
    "license": "OPL-1",
    "depends": ["mail", "document_knowledge", "html_editor"],
    "data": [
        "security/document_page_security.xml",
        "security/ir.model.access.csv",
        "wizard/document_page_create_menu.xml",
        "wizard/document_page_show_diff.xml",
        "views/document_page.xml",
        "views/document_page_category.xml",
        "views/document_page_history.xml",
        "views/report_document_page.xml",
    ],
    "demo": ["demo/document_page.xml"],
    "assets": {
        "web._assets_primary_variables": [
            "document_page/static/src/**/document_page_variables.scss",
        ],
        "web.assets_backend": [
            "document_page/static/src/scss/document_page.scss",
            "document_page/static/src/js/document_page_kanban_controller.esm.js",
            "document_page/static/src/js/document_page_kanban_view.esm.js",
        ],
    },
}
