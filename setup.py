import os
import sys

from setuptools import setup, find_packages

extra = {}
if sys.version_info >= (3, 0):
    extra.update(
        use_2to3=True,
    )

readme = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(name='Dogpile',
      version=0.1,
      description="A 'Dogpile' lock, typically used as a component of a larger caching solution",
      long_description=file(readme).read(),
      classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      ],
      keywords='caching',
      author='Mike Bayer',
      author_email='mike_mp@zzzcomputing.com',
      url='http://bitbucket.org/zzzeek/dogpile',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      zip_safe=False,
      install_requires=[],
      test_suite='nose.collector',
      tests_require=tests_require,
      **extra
)