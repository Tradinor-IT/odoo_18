{
    'name': 'Custom Pricelist Access Control',
    'version': '1.0',
    'summary': 'Restrict access to price lists based on user roles',
    'author': 'elhadi73',
    'website': 'https://yourwebsite.com',
    'category': 'Sales',
    'depends': ['base', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/pricelist_security.xml',
        'views/pricelist_view.xml',
    ],
    'installable': True,
    'application': False,
}
