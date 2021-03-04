#!/usr/bin/env python

from setuptools import setup
import algocli

setup(name='algocli',
      version=algocli.__version__,
      description="Print common known algorithms to the command line",
      long_description='',
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Topic :: Documentation",
      ],
      keywords='algocli algorithms console command line',
      author='Emanuel Ramirez Alsina',
      author_email='eramirez2718@gmail.com',
      maintainer='Emanuel Ramirez Alsina',
      maintainer_email='eramirez2718@gmail.com',
      url='https://github.com/eramirez2718/algocli',
      license='MIT',
      packages=['algocli'],
      zip_safe=False,
      install_requires=[
          'Pygments'
          'bs4',
          'requests',
          'setuptools',
      ],
      entry_points={
          'console_scripts': [
              'algocli = algocli.main:algoCLI',
          ]
      }
)
