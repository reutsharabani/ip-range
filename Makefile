.PHONY: build test clean

clean:
	git clean -xdf -e .idea

test:
	python setup.py test

build:
	python setup.py bdist_wheel
