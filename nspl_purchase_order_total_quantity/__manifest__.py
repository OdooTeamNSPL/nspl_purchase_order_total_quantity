{
    'name': 'Purchase Order total Quantity Summary',
    'version': '18.0',
    'description': """
Purchase Order Quantity Summary
This module enhances the Purchase Order form by adding a summary of key quantity fields for better tracking and decision making.

Key Features:
- Displays total demand quantity (ordered quantity).
- Shows total received and billed quantities.
- Calculates and displays pending receipt and pending bill quantities.
- All quantity fields are auto-calculated and read-only.
- Helps procurement and finance teams easily track PO progress.

""",
    'summary': 'Displays received, billed, and pending quantities on purchase orders.',
    'category': 'Purchases',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'contributors': 'Mohit Nare',
    'website': 'http://namahsoftech.com/',
    'license': 'OPL-1',
    'price': 9.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_view.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
