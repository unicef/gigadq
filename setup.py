from setuptools import find_packages, setup
setup(
    name='gigadq',
    packages=find_packages(),
    version='0.1.0',
    description='Giga DQ',
    author='Shilpa',
    license='',
    install_requires=['uuid'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1','pandas'],
    test_suite='tests'
)