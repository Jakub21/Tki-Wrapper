from setuptools import setup, find_packages

long_description = open('README.md', 'r').read()

setup(
  name = 'TkiWrapper',
  description = 'Create grid-based GUIs faster and easier',
  long_description = long_description,
  version = '1.0.0',
  license = 'MIT',
  author = 'Jakub21',
  url = 'https://github.com/Jakub21',
  packages = find_packages(),
)
