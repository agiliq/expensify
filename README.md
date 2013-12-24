=======
Expensify
==========

[![Build Status](https://travis-ci.org/agiliq/expensify.png?branch=master)](https://travis-ci.org/agiliq/expensify)
[![Coverage Status](https://coveralls.io/repos/agiliq/expensify/badge.png)](https://coveralls.io/r/agiliq/expensify)

### What is it?

A Django app to claim and track your reimbursements and expense claims.

### Features

1. Users can enter their reimbursements
2. Users can see their past reimbursements
3. User can be marked as admin who can see all expense claims.
4. Set a per person yearly limit
5. Admin can mark a expense claim as paid.
6. Admin gets email when a new expense claim is added.
7. User gets email when an expense claim is marked as paid by the user.

### Installation

1. pip install -r requirements.txt
2. create a `expensify/local_settings.py` and fill it with correct values.
3. Add email settings to send email.
3. (Optionally) Update `OPENID_SSO_SERVER_URL`


### requirements

See requirements.txt

