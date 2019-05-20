from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name = 'TkiWrapper',
    description = 'Create grid-based GUIs faster and easier',
    long_description = long_description,
    version = '0.5',
    license = 'MIT',
    author = 'Jakub21',
    url = 'https://github.com/Jakub21',
    packages = find_packages(),
)
