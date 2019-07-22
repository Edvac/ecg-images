from distutils.core import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='ecg_to_images',
   version='1.0',
   description='A package to create images',
   license="MIT",
   long_description=long_description,
   author='Man Foo',
   author_email='g-politis@outlook.com',
   url="not availableyet",
   packages=['ecg_to_images'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)