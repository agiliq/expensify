from distutils.core import setup

setup(
    name="expensify",
    version="1.0",
    packages=['exapp', ],
    package_dir={'exapp': 'exapp'},
    package_data={'exapp': ['templates/*.html',
                            'templates/leave_tracker/*.html',
                           ]
    },
    author="Agiliq Solutions",
    author_email="hello@agiliq.com",
    description="A Django app to claim and track your reimbursements and expense claims",
    long_description=
    """
A Django app to claim and track your reimbursements and expense claims.
""",)