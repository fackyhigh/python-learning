from setuptools import setup, find_packages

with open('README.rst') as file:
    readme = file.read()

setup(
    name='hr',
    version='1.0.0',
    description='CLI tool for exporting user data',
    long_description=readme,
    author='Konstantin Nemanov',
    author_email='hello@world.com',
    packages=find_packages('src'),
    package_dir={'', 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': ['hr=hr.cli:main'],
    }
)

