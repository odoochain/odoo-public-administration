# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class transaction_type(models.Model):
    """Transaction Type"""

    _name = 'public_budget.transaction_type'
    _description = 'Transaction Type'

    name = fields.Char(
        string='Name',
        required=True,
        translate=True
        )
    with_amount_restriction = fields.Boolean(
        string='With Amount Restriction?'
        )
    with_salary_advance = fields.Boolean(
        string='With Advance Salary'
        )
    with_advance_payment = fields.Boolean(
        string='With advance payment?'
        )
    advance_account_id = fields.Many2one(
        'account.account',
        string='Advance Account',
        context={'default_type': 'other'},
        domain=[('type', '=', 'other'), ('user_type.report_type', 'in', ['asset'])]
        )
    amount_restriction_ids = fields.One2many(
        'public_budget.transaction_type_amo_rest',
        'transaction_type_id',
        string='Amount Restrictions'
        )

    _constraints = [
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: