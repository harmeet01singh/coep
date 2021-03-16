from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='vml_modules',
  version='0.0.2',
  description='Stores data in csv format',
#   long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Rohan Pol',
  author_email='rohanpol36@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='VMathlab', 
  packages=find_packages(),
  install_requires=[''] 
)