# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 15:20:19 2022

@author: panna
"""

from setuptools import setup

setup(
   name='EasyRoman',
   version='0.0.1',
   license="MIT",
   description='A simple library written for python to interchange Roman and Integer Numbers',
   author='Pannag Desai',
   long_description="This library is a simple interface to convert Roman to integer or Integer to Roman",
   author_email='pannag.desai@outlook.com',
   packages=['EasyRoman'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)
