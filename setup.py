import os
from distutils.core import setup
from distutils.command.dist import sdist

import tengine  # safe, because __init__.py contains no import statements


class my_sdist(sdist):
    def make_distribution(self):
        for path in self.filelist.files:
            os.chmod(path, 0o644)
        sdist.make_distribution(self)


setup(
    cmdclass={'sdist': my_sdist},
    name='tengine',
    version=tengine.__version__,
    description=tengine.__doc__.split('\n', 1)[0],
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    license='MIT',
    author='Reece Chimento',
    url='http://github.com/reecechimento/python-tengine/',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.9',
        ],
    packages=[
        'tengine',
        'tengine.data',
        'tengine.tests',
        ],
    package_data={
        'tengine': ['documentation/*.rst'],
        'tengine.data': ['*.yml', '*.csv', '*.json'],
        'tengine.tests': ['data/*'],
        },
    install_requires=[
        'numpy',
        'click'
        ],
)
