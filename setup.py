from setuptools import find_packages, setup

setup(
    name='Votegen',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='Library to generate Inequalities to use in PyNormaliz',
    author='Emil Breustedt',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests')