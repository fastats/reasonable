
from distutils.core import setup

MAJOR = 2017
MINOR = 1
MICRO = ''

version = '.'.join(map(str, [MAJOR, MINOR]))
if MICRO:
  version += MICRO


def setup_package():
    setup(
      name='reasonable',
      packages=['reasonable'],
      version=version,
      description='Reasonable float handling for Hypothesis testing',
      author='Dave Willmer',
      author_email='dave.willmer@gmail.com',
      url='https://github.com/fastats/reasonable',
      download_url='https://github.com/fastats/reasonable/archive/2017.1.tar.gz',
      keywords=['reasonable', 'hypothesis', 'generative testing'],
      classifiers=[]
    )


if __name__ == '__main__':
    setup_package()
