.PHONY: test upload clean boot

test:
	sh -c '. venv/bin/activate; pytest'

upload: test
	python setup.py sdist bdist_wheel upload
	make clean
	
register:
	python setup.py register

clean:
	rm -f MANIFEST
	rm -rf build dist
	
boot: _venv
	venv/bin/pip install -r requirements.txt
	make clean

_venv:
	virtualenv -p python3 venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
