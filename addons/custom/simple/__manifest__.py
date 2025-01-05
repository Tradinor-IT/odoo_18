{
    'name': 'Simple Book Manager',
    'version': '1.0',
    'author': 'ElHadi73',
    'website': 'https://yourwebsite.com',
    'summary': 'Manage a list of books',
    'description': """
A simple module to manage books.
""",
    'depends': ['base'],  # Minimal dependency
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
    ],
    'installable': True,
    'application': True,
}
