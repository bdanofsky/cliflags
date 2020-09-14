from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='cliflags',
      version='0.1',
      description='JSON based flags management for CLI applications',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='JSON base flag management',
      url='http://github.com/bdanofsky/cliflags',
      author='Brad Danofsky',
      author_email='bdanofsky@gmail.com',
      license='MIT',
      packages=['cliflags'],
      install_requires=[
          #'python-jsonschema-objects',
      ],
      test_suite='nose.collector',
      tests_require=[
          #'nose',
          #'nose-cover3'
      ],
      entry_points={
          #'console_scripts': ['funniest-joke=funniest.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
