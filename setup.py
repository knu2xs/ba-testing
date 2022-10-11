from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='ba_testing',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Scripts and tools to streamline Business Analyst Quality Assurance testing.',
    long_description=long_description,
    author='Esri Business Analyst Deveopment Team',
    license='Apache 2.0',
)
