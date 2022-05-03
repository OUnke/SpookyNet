#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='spookynet',
      version='1.0',
      description=('SpookyNet: Learning force fields with electronic degrees '
                   'of freedom and nonlocal effects'),
      author=('Unke, O. T., Chmiela, S., Gastegger, M., Schütt, K. T.,'
              ' Sauceda, H. E., & Müller, K. R.'),
      url='https://github.com/OUnke/SpookyNet',
      packages=find_packages(),
      python_requires=">=3.7",
      install_requires=[
          "ase>=3.22.1",
          "numpy>=1.22.3",
          "scikit-learn>=1.0.2",
          "torch>=1.11.0",
      ],
      license="MIT",
      package_data={'spookynet.modules': ['d4data/*.pth']},
)

