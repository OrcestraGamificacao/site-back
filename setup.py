import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# with open(os.path.join(here, 'README.md')) as f:
#     README = f.read()

# requires = [
#     'sqlalchemy',
#     'psycopg2',
#     'alembic',
#     'flask',
#     'flask-sqlalchemy'
# ]

# tests_require = [
#     'pytest',  # includes virtualenv
#     'pytest-cov'
# ]


setup(
    name='site-backend',
    version='0.1.0',
    description='Backend site orcestra',
    author='Orcestra',
    author_email='projetos@orcestra.com.br',
    packages=find_packages()
)
