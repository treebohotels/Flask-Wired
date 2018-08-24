# Flask-Wired #

Flask-Wired is an opinionated composable supporting framework for Flask.

[![Build Status](https://travis-ci.org/treebohotels/Flask-Wired.svg?branch=master)](https://travis-ci.org/treebohotels/Flask-Wired)

### What is this repository for? ###

* Quick summary
Flask-Wired is designed to be used Flask to simplify initial bootstrap wiring for microservices by
	1. Taking standardized way of wiring the components like db connections, transactions, serializers, service discovery, log aggregation etc.
	2. Provide a place for the boilerplate code to be maintained in standardized way & upgrade seemlessly
	3. Reduce the time taken for bootstrapping by simplifying the service template. Ex: defaults for app.py, manage.py will be provided by Flask-Wired. 
* Version
Initial version supports the following:
	1. db connection
	2. marshmallow as default serializer
	3. Flask blue prints registration
	4. Structured Logging
	5. Request Id generator

### How do I get set up? ###

* Summary of set up
	1. pip install Flask-Wired
	2. configure the extensions in settings.py as usual.
	3. follow documentation for additional keys supported by Flask-Wired.
	4. Keep Flask-Wired version upto date with latest & greatest.
Note: Do not add direct dependency to Flask in your project directly.
* Configuration
Additional keys supported in settings.py by Flask-Wired:
	1. BLUEPRINTS
* Dependencies
	1. flask
	2. flask-script
	3. flask-migrate
* Deployment instructions
Package & Deploy your code as usual.

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
