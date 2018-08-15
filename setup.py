import setuptools


def read_file(name):
    with open(name) as fp:
        return fp.read()

setuptools.setup(
    name='iprange',
    version='0.1',
    long_description=read_file('README.md'),
    packages=['iprange'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner']
)
