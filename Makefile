.PHONY: test upload clean clean-pyc boot lint register _venv

test:
	@printf "#\n# Testing\n#\n"
	pytest

upload: test
	python setup.py sdist bdist_wheel upload
	make clean

lint:
	flake8

register:
	python setup.py register

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-pyc
	rm -f MANIFEST
	rm -rf build dist
	
boot: _venv
	venv/bin/pip install -r requirements.txt
	make clean

_venv:
	virtualenv -p python3 venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
