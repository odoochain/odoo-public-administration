# -*- coding: utf-8 -*-
{
    'name': 'Public Budget',
    'license': 'AGPL-3',
    'version': '9.0.1.10.0',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'category': 'Accounting & Finance',
    'depends': [
        'portal',
        'account',
        'account_check',
        'account_payment_group_document',
        'account_asset',
        'hr_public_holidays',
        'report_aeroo',
        'account_statement_aeroo_report',
        'report_custom_filename',
        # estrictamente solo requerido por algunos campos en vista de partner
        'l10n_ar_account',
        # solo para el reporte de ordenes de pago que imprime el dato de la
        # validacion
        'l10n_ar_afipws_fe',
        # mas que nada para datos demo y porque lo queremos
        'l10n_ar_states',
        # solo requerido para establecer datos demo en cia y hacer que las ret
        # no sean obligatorias en borrador
        'l10n_ar_account_withholding',
        # usado por algunos reportes como el de cheques y retenciones
        'l10n_ar_aeroo_base',
        # agregamos este porque se auto instala y termina instalando
        # date range y entonces tenemos que agregar regla de portal de date
        # range para que no de error. Si en un futuro evitamos que este modulo
        # se auto instale en producción, entonces podemos sacarlo como dep
        'l10n_ar_account_vat_ledger',
    ],
    'data': [
        'security/public_budget_group.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'security/hide_groups.xml',
        'wizard/transaction_definitive_make_invoice_view.xml',
        'wizard/transaction_definitive_mass_invoice_create_view.xml',
        'wizard/budget_analysis_wizard_view.xml',
        'wizard/avance_request_report_wizard_view.xml',
        'wizard/public_budget_preventive_changeposition_view.xml',
        'wizard/account_check_debit_view.xml',
        'reports/advance_request_analysis_view.xml',
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
        'reports/asset_report.xml',
        'reports/check_report.xml',
        'reports/payment_order_list.xml',
        'reports/public_budget_budget_report_view_3.xml',
        'view/inventory_rule_view.xml',
        'view/account_invoice_view.xml',
        'view/advance_request_type_view.xml',
        'view/advance_request_view.xml',
        'view/transaction_type_view.xml',
        'view/transaction_type_amo_rest_view.xml',
        'view/advance_return_view.xml',
        'view/expedient_category_view.xml',
        'view/location_view.xml',
        'view/budget_modification_detail_view.xml',
        'view/funding_move_view.xml',
        'view/account_invoice_line_view.xml',
        'view/rest_type_view.xml',
        'view/users_view.xml',
        'view/preventive_line_view.xml',
        'view/budget_position_view.xml',
        'view/company_view.xml',
        'view/budget_detail_view.xml',
        'view/budget_prec_detail_view.xml',
        'view/definitive_line_view.xml',
        'view/transaction_view.xml',
        'view/budget_position_category_view.xml',
        'view/budget_view.xml',
        'view/remit_view.xml',
        'view/budget_pos_exc_rest_view.xml',
        'view/budget_modification_view.xml',
        'view/expedient_view.xml',
        'view/expedient_founder_view.xml',
        'view/res_partner_view.xml',
        'view/account_asset_view.xml',
        'view/account_check_view.xml',
        'view/account_payment_group_view.xml',
        'view/account_payment_view.xml',
        'view/hr_public_holidays_view.xml',
        'view/custom_views.xml',
        'view/public_budget_menuitem.xml',
        'view/public_budget_actions.xml',
        'view/account_checkbook_view.xml',
        'data/sequence.xml',
        'data/expedient_category.xml',
        'data/expedient_founder.xml',
        'data/position_category.xml',
        'data/position_exc_restrictions.xml',
        'data/ir_config_parameter_data.xml',
        'data/server_actions_data.xml',
    ],
    'demo': [
        'demo/res_company_demo.xml',
        'demo/public_budget.location.csv',
        'demo/res_users_demo.xml',
        # once admin is in sipreco company, we load chart of account
        'demo/account_chart_template.yml',
        'demo/res_partner_demo.xml',
        'demo/res.partner.csv',
        'demo/account_account_demo.xml',
        'demo/account_payment_receiptbook_demo.xml',
        'demo/public_budget.transaction_type.csv',
        'demo/public_budget.expedient.csv',
        'demo/public_budget.budget_position.csv',
        'demo/public_budget.budget.csv',
        'demo/public_budget.budget_detail.csv',
        'demo/public_budget_transaction_demo.xml',
        'demo/public_budget.preventive_line.csv',
        'demo/public_budget_definitive_line_demo.xml',
        'demo/public_budget.remit.csv',
        'demo/public_budget.budget_modification.csv',
        'demo/public_budget.budget_modification_detail.csv',
        'demo/account_journal_demo.xml',
        'demo/advance_request_type.xml',
        'demo/advance_request.xml',
    ],
    'test': [],
    'installable': True,
}
