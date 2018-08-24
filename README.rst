===========
Flask-Wired
===========
Flask-Wired is an opinionated composable supporting framework for Flask.

.. image:: https://travis-ci.org/treebohotels/Flask-Wired.svg?branch=master

Quick summary
~~~~~~~~~~~~~

Flask-Wired is designed to be used Flask to simplify initial bootstrap wiring for Micro Services by

1. Taking a standardized way of wiring the components like DB connections, transactions, serializers, service discovery, log aggregation etc.
2. Provide a place for the boilerplate code to be maintained in a standardized way & upgrade seamlessly
3. Reduce the time taken for bootstrapping by simplifying the service template. Ex: defaults for app.py, manage.py will be provided by Flask-Wired.

Initial version supports the following:

1. DB connection
2. marshmallow as default serializer
3. Flask blueprints registration
4. Structured Logging
5. Request Id generator

How do I install?
~~~~~~~~~~~~~~~~~

.. code-block:: text

	pip install Flask-Wired

Configuration
~~~~~~~~~~~~~

1. configure the extensions in settings.py as usual.
2. follow the documentation for additional keys supported by Flask-Wired.
3. Keep Flask-Wired version up to date with latest & greatest.

.. note:: Do not add a direct dependency to Flask in your project directly.

Dependencies
~~~~~~~~~~~~

1. Flask
2. Flask-Script
3. Flask-Migrate

Deployment instructions
~~~~~~~~~~~~~~~~~~~~~~~

Package & Deploy your code the same way as with Flask.

Contribution guidelines
~~~~~~~~~~~~~~~~~~~~~~~

* Writing tests - TBD
* Code review - TBD
* Other guidelines - TBD

Who do I talk to?
~~~~~~~~~~~~~~~~~

* Repo owner or admin
* Other community or team contact
