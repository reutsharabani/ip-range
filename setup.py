import setuptools


def read_file(name):
    with open(name) as fp:
        return fp.read()

setuptools.setup(
    name='ip-range',
    version='0.0.6',
    long_description=read_file('README.md'),
    packages=['iprange'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    author="Reut Sharabani",
    author_email="reut.sharabani@gmail.com",
    description="library to handle ip ranges (using `ipaddress`)",
    url="https://github.com/reutsharabani/ip-range",
    classifiers=(
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
    ),
)
