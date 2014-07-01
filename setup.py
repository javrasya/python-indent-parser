__author__ = 'ahmetdal'

from setuptools import setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='python-indent-parser',
    version='1.0.0',
    description='Python Indent Parser',
    author='Ahmet DAL',
    author_email='ceahmetdal@gmail.com',
    url='https://github.com/javrasya/python-indent-parser',
    keywords=["python", "indent", "indent_parser"],
    install_requires=[
    ],
    packages=['src', 'resources'],
    include_package_data=True,
    zip_safe=False,
    license='GPL',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ]
)