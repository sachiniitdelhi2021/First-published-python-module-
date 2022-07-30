
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='maths_ops',
    version='0.0.1',
    author='Sachin Dangi',
    email='sachiniit36@gmail.com',
    description='This python module contains total of 10  functions for doing basic mathematical operations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    keywords=['maths','maths_ops','maths_operations'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    py_modules=['maths_ops'],
    package_dir={'': 'maths_ops'}
)