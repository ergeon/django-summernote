import sys
from setuptools import setup, find_packages
from django_summernote import version, PROJECT


MODULE_NAME = 'django_summernote'
PACKAGE_DATA = list()
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 5.2',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]

setup(
    name=PROJECT,
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    author='django-summernote contributors',
    maintainer='django-summernote maintainers',
    url='http://github.com/summernote/django-summernote',

    description='Summernote plugin for Django',
    classifiers=CLASSIFIERS,

    python_requires='>=3.12',
    install_requires=['django>=5.2,<6.0', 'bleach'],
    extras_require={
        'dev': [
            'django-dummy-plug',
            'pytest',
            'pytest-django',
        ]
    },
)
