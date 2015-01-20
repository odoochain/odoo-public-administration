# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class expedient_founder(models.Model):
    """Expedient Founder"""

    _name = 'public_budget.expedient_founder'
    _description = 'Expedient Founder'

    name = fields.Char(
        string='Name',
        required=True
        )

    _constraints = [
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: