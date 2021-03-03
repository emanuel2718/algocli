#!/usr/bin/env python

from setuptools import setup
import algocli

setup(name='algocli',
      version=algocli.__version__,
      description="Print common known algorithms to the command line",
      long_description='',
      classifiers=[
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Topic :: Documentation",
      ],
      classifiers=[],
      keywords='algocli algorithms console command line',
      author='Emanuel Ramirez Alsina',
      author_email='eramirez2718@gmail.com',
      url='https://github.com/eramirez2718/algocli',
      license='MIT',
      packages=['algocli'],
      zip_safe=False,
      install_requires=[
          'setuptools',
          'requests',
          'bs4',
      ],
      entry_points={
          'console_scripts': [
              'algocli = algocli.main:algoCLI',
          ]
      }
)
