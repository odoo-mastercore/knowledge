# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0)
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
###############################################################################


{
    "name": "Documents Knowledge",
    "version": "19.0.1.0.0",
    "category": "Knowledge",
    "summary": "Provide centralized document permissions category.",
    "description": "Base knowledge configuration with centralized document access group.",
    "author": "Mastercore Sinapsys Global®",
    "website": "https://www.mastercore.co",
    "license": "OPL-1",
    "depends": ["base"],
    "data": [
        "data/ir_module_category.xml",
        "security/document_knowledge_security.xml",
        "data/res_users.xml",
        "views/document_knowledge.xml",
        "views/res_config.xml",
    ],
    "demo": ["demo/document_knowledge.xml"],
    "installable": True,
    "application": True,
}
