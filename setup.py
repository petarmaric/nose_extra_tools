import sys
from setuptools import setup
from requirements_utils import parse_requirements


if sys.version_info < (2, 6):
    print 'ERROR: nose_extra_tools requires at least Python 2.6 to run.'
    sys.exit(1)


setup(
    name='nose_extra_tools',
    version='1.0.0',
    url='https://bitbucket.org/petar/nose_extra_tools',
    license='BSD',
    author='Petar Maric',
    author_email='petarmaric@uns.ac.rs',
    description='Extra testing goodies for nose.tools',
    long_description=open('README').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    platforms='any',
    py_modules=['nose_extra_tools'],
    install_requires = parse_requirements('requirements.txt'),
)
