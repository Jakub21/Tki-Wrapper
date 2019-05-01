from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name = 'TkiWrapper',
    description = 'TkInter wrapper. Create TK grid-based GUIs faster',
    long_description = long_description,
    version = '0.1',
    license = 'MIT',
    author = 'Jakub21',
    author_email = 'jakubp2101@gmail.com',
    url = 'https://github.com/Jakub21',
    packages = ['TkiWrapper'],
)
