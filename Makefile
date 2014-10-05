
PYTHON=`which python3`

all:
	@echo "make source - Create source package"
	@echo "make install - Install on local system"
	@echo "make clean - Get rid of scratch and byte files"


source:
	$(PYTHON) setup.py sdist

upload:
	$(PYTHON) setup.py register sdist upload

install:
	$(PYTHON) setup.py install

clean:
	$(PYTHON) setup.py clean
	find . -name '*.pyc' -delete
