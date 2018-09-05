from setuptools import setup

setup(name='broom',
      version='0.1',
      description='Tidy your linear models in Python',
      url='http://github.com/diengiau/broom',
      author='Dien Giau Bui',
      author_email='buidiengiau@gmail.com',
      license='MIT',
      packages=['broom'],
	  install_requires=[
          'pandas', 'patsy', 'numpy', 'statsmodels'
      ],
      zip_safe=False)