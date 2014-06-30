from setuptools import setup
#from distutils.core import setup
import os


def file_walk_relative(top, remove=''):
    """
    Returns a generator of files from the top of the tree, removing
    the given prefix from the root/file result.

    Duplicated from Cartopy's setup.py.

    """
    for root, dirs, files in os.walk(top):
        for file in files:
            yield os.path.join(root, file).replace(remove, '')


setup(
    name='tephi',
    version='0.1.0',
    url='https://github.com/SciTools/tephi',
    author='Bill Little',
    author_email='bill.james.little@gmail.com',
    packages=['tephi', 'tephi.tests'],
    package_dir={'': 'lib'},
    #package_data={'': list(file_walk_relative('etc'))},
    package_data={'tephi': ['etc/test_data/*.txt'] + ['etc/test_results/*.pkl']},
    classifiers=['License :: OSI Approved :: '
                 'GNU Lesser General Public License v3 (LGPLv3)'],
    description='Tephigram plotting in Python',
    long_description=open('README.rst').read(),
    test_suite='tephi.tests',
    #zip_safe=False
)
