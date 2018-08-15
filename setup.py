import setuptools


setuptools.setup(
    name='iprange',
    version='0.1',
    long_description=read_file('README.md', splitlines=False),
    packages=['iprange'],
    tests_require=['pytest']),
    setup_requires=['pytest-runner'],
)
