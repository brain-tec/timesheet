{
    'name': 'HR Timesheet Sheet Attendance',
    'version': '11.0.0.0.2',
    'category': 'Human Resources',
    'sequence': 80,
    'license': 'AGPL-3',
    "author": "BizzAppDev, "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/timesheet",
    'depends': [
        'hr_attendance',
        'hr_timesheet_sheet'
    ],
    'data': [
        'views/assets.xml',
        'views/hr_timesheet_sheet_view.xml',
        'views/hr_attendance_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
