.PHONY: build test clean

clean:
	git clean -xdf -e .idea

test:
	python setup.py test

build: test
	python setup.py bdist_wheel

upload: build
	python -m twine upload dist/*
