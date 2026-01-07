# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0) 
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################

{
    "name": "Document Page Access Group",
    "summary": "Choose groups to access document pages",
    "version": "19.0.1.0.1",
    "category": "document_knowledge",
    "website": "https://github.com/OCA/knowledge",
    "author": "Sygel, Creu Blanca, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "document_page",
        "document_knowledge",
    ],
    "data": [
          "views/document_page.xml", 
          "security/security.xml"
     ],
}