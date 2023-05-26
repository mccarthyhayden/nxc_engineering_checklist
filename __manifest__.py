{
    'name': 'NXC Engineering Checklist Addon',
    'version': '15.0',
    'category': 'manufacturing',
    'summary': 'Adds design checklist, design build checklist, product configuration checklist, and approvals to the Manufacturing Order model.',
    'description': 'This custom module was developed for Next Chapter Manufacturing to prompt users with engineering checklists on Manufacturing Orders. The addon includes stop-gates to prevent order confirmation prior to checklists completion.',
    'author': 'Hayden McCarthy',
    'website': 'https://www.nxcmfg.com',
    'license': 'AGPL-3',
    'depends': ['mrp'],
    'data': [
        'views/view_nxc_engineering_checklist_mrp_production_form.xml',
    ],
    'installable': True,
    'auto_install': False,
}

