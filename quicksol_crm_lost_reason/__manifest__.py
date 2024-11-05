{
    'name': 'CRM Custom Lost Reason',
    'version': '17.0.1.0.0',
    'category': 'Sales/CRM',
    'sequence' : '1',
    'price': 10.0,
    'currency': 'USD',
    'summary': 'Add custom lost reasons to CRM leads and opportunities',
    'support': 'quicksol.odoo.help@gmail.com',
    'description': """
CRM Lost Reason Extension
========================
* Add custom reasons when marking leads/opportunities as lost
* View detailed lost reasons in lead/opportunity form
* Simple and effective lost reason tracking
    """,
    'author': 'QuickSol Technologies',
    'website': 'https://quicksol.ca',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_lost_reason_data.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
'images': ['static/description/custom_field.png','static/description/mark_lost.png','static/description/icon.png','static/description/banner.png'],
    'icon': 'quicksol_crm_lost_reason/static/description/icon.png',
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}