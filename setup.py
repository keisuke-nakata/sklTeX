from setuptools import setup

setup(name='sklTeX',
      version='0.1',
      description='convert sklearn models into TeX',
      keywords='sklearn scikit-learn model latex pdf',
      url='https://github.com/keisuke-nakata/sklTeX',
      author='NAKATA Keisuke',
      author_email='keisuke.nakata.919@gmail.com',
      license='BSD',
      packages=['sklTeX'],
      install_requires=[
          'numpy',
          'scipy',
          'sklearn',
          'latex'
      ],
      zip_safe=False)
