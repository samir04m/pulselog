import os

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', '1234')
STAFF_PASSWORD = os.environ.get('STAFF_PASSWORD', '1234')

users = [
    {
        'username': 'admin',
        'password': ADMIN_PASSWORD,
        'is_superuser': True,
        'is_staff': True,
    },
    {
        'username': 'samir',
        'password': ADMIN_PASSWORD,
        'is_superuser': True,
        'is_staff': True,
    },
]    