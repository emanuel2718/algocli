from setuptools import setup

setup(name='algocli',
      version='0.1',
      description="Print common known algorithms to the command line",
      long_description='',
      classifiers=[],
      keywords='python algorithms cli',
      author='Emanuel Ramirez Alsina',
      author_email='eramirez2718@gmail.com',
      url='https://github.com/eramirez2718/algocli',
      license='MIT',
      packages=['algocli'],
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      algocli = algocli.main:main
      """,
)
