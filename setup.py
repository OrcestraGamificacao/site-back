import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    'flask',
    'sqlalchemy',
    'flask-sqlalchemy',
    'alembic',
    'psycopg2'
]

setup(
    name='site-backend',
    version='0.1.0',
    description='Backend site orcestra',
    author='Orcestra',
    author_email='projetos@orcestra.com.br',
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    packages=find_packages()
)
