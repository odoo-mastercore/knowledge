# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0) 
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################

{
    "name": "Document Page Group",
    "summary": """
        Define access groups on documents""",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "author": "Creu Blanca,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/knowledge",
    "depends": ["document_page"],
    "data": [
          "security/document_page_security.xml", 
          "views/document_page.xml"
     ],
}