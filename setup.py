from setuptools import setup, find_packages

setup(name='django-softdelete',
      version='0.4.1',
      description='Soft delete support for Django ORM, with undelete.',
      author='Steve Coursen',
      author_email='smcoursen@gmail.com',
      maintainer='Steve Coursen',
      maintainer_email='smcoursen@gmail.com',
      license="BSD",
      url="https://github.com/scoursen/django-softdelete",
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          'Framework :: Django',
          'License :: OSI Approved :: BSD License',
          'Environment :: Web Environment',
      ]
      )
