.PHONY: build clean test-publish publish

build:
	python setup.py sdist bdist_wheel

clean:
	rm -fr build findersel.egg-info dist

test-publish:
	twine upload --repository testpypi dist/*

publish:
	twine upload dist/*
