

{
    "name": "Leuwint Theme",
    "description": """Minimalist and elegant backend theme for Odoo 15, Backend Theme, Theme""",
    "summary": "Leuwint Theme is an attractive theme for backend",
    "category": "Themes/Backend",
    "version": "15.0.1.0.0",
    'author': 'Manu S',
    'company': 'Leuwint',
    'maintainer': 'Leuwint',
    'website': "https://leuwint.com/",
    "depends": ['base', 'web', 'mail'],
    "data": [
        'views/res_config_settings.xml',
    ],
    'assets': {

        'web.assets_backend': [
                'leuwint_theme/static/src/layout/style/login.scss',
                'leuwint_theme/static/src/layout/style/layout_colors.scss',
                'leuwint_theme/static/src/components/app_menu/menu_order.css',
                'leuwint_theme/static/src/layout/style/layout_style.scss',
                'leuwint_theme/static/src/layout/style/sidebar.scss',
                'leuwint_theme/static/src/components/app_menu/search_apps.js',
        ],
        'web.assets_qweb': [
                'leuwint_theme/static/src/components/app_menu/side_menu.xml',

        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.gif',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
