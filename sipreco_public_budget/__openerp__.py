# -*- coding: utf-8 -*-
{'active': False,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'category': 'Accounting & Finance',
    'data': [
        'wizard/transaction_definitive_make_invoice_view.xml',
        'wizard/account_check_handed_wizard_view.xml',
        'reports/stylesheet.xml',
        'reports/payment_order_report.xml',
        'reports/remit_report.xml',
        'reports/expedient_report.xml',
        'reports/transaction_report.xml',
        'reports/payment_receipt_report.xml',
        'reports/statement_report.xml',
        'reports/budget_report.xml',
        'reports/advance_request_report.xml',
        'reports/advance_return_report.xml',
        'reports/liquidation_report.xml',
        'reports/advance_request_debt_report.xml',
        'views/res_partner_view.xml',
        'views/custom_views.xml',
        'views/account_asset_view.xml',
        'views/account_voucher_view.xml',
        'views/account_check_view.xml',
        'views/budget_view.xml',
        'views/remit_view.xml',
        'views/expedient_view.xml',
        'views/transaction_view.xml',
        'views/preventive_line_view.xml',
        'views/transaction_type_view.xml',
        'views/advance_request_view.xml',
        'views/advance_return_view.xml',
        'views/account_checkbook_view.xml',
        'views/invoice_view.xml',
        'workflow/account_voucher_workflow.xml',
        'workflow/account_check_workflow.xml',
        'data/ir_parameters.xml',
        'data/expedient_category.xml',
        'data/expedient_founder.xml',
        'data/position_category.xml',
        'data/position_exc_restrictions.xml',
        'data/account_account.xml',
        'data/transaction_type.xml',
        'data/journal_sequence.xml',
        'data/account_journal.xml',
        'data/account_checbook.xml',
        'data/taxes.xml',
        'data/account_tax_withholding.xml',
        'data/account_properties.xml',
        # we can not make it compatible with demo data and test
        # 'data/account_fiscal_year.xml',
        'data/res_partner.xml',
        'data/tax_settlement.xml',
        'data/advance_request_type.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/document_type.xml',
    ],
    'demo': [
        'demo/company_demo.xml',
        'demo/res.partner.csv',
        'demo/res_partner.xml',
        'demo/public_budget.location.csv',
        'demo/user_demo.xml',
        'demo/account.account.csv',
        'demo/account.journal.csv',
        'demo/account.checkbook.csv',
        'demo/account_properties.xml',
        'demo/account_period.xml',
        'demo/receipt_demo.xml',
        'demo/taxes.xml',
        'demo/tax_settlement.xml',
        'demo/account.tax.withholding.csv',
        'demo/public_budget.transaction_type.csv',
        'demo/public_budget.expedient.csv',
        'demo/public_budget.budget_position.csv',
        'demo/public_budget.budget.csv',
        'demo/public_budget_demo.xml',
        'demo/public_budget.budget_detail.csv',
        'demo/public_budget.transaction.csv',
        'demo/public_budget.preventive_line.csv',
        'demo/public_budget.definitive_line.csv',
        'demo/public_budget.remit.csv',
        'demo/public_budget.budget_modification.csv',
        'demo/public_budget.budget_modification_detail.csv',
        'demo/advance_request_type.xml',
        'demo/advance_request.xml',
        'demo/partners_without_doc/res.partner.csv',
    ],
    'depends': [
        'l10n_ar_invoice',
        'l10n_ar_aeroo_voucher',
        'public_budget',
        'account_voucher_constraint',
        'account_asset',
        'account_statement_aeroo_report',
        'share',
        'account_statement_move_import',
        'web_m2x_options',
        'account_tax_settlement_withholding',
    ],
    'description': '''
Public Budget Sipreco Customizations
====================================
Customizaciones especificas al modulo public_budget para SIPRECO
* Agregar punto de venta y numero de factura en wizar de generacion de factura
''',
    'installable': True,
    'name': 'Public Budget Sipreco Customizations',
    'test': [],
    'version': '8.0.1.10.1'}
