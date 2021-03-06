{
    'name': 'Travel agency module',
    'version': '1.1',
    'author': 'Stefano',
    'description': 'A module to manage hotel bookings and other useful features',
    'category': 'Generic Modules/Others',
    'website': '',
    'depends': [
        'base_setup',
        'board',
        'mail',
        'resource'
    ],
    'data': [
        'rooms_info_view.xml',
        'booking_management_view.xml',
    ],
    'demo': [],
    'test': [],
    # 'auto_install': False,
    'active': False,
    'installable': True,
}
