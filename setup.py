from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='WiSync',
   version='1.0.0.dev1',
   python_requires='>=3',
   description='You favorite home automation platform.',
   license="MIT",
   long_description=long_description,
   author='ArnyminerZ',
   author_email='arnyminer.z@gmail.com',
   url="https://github.com/CMakerA/WiSync",
   packages=['WiSync'],  #same as name
   install_requires=['pygame'], #external packages as dependencies
)
