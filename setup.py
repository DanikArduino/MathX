from setuptools import setup, find_packages
setup(
    name='mathx',
    version='1.0.0',
    author='daniil',
    author_email='danik20110723@gmail.com',
    url='https://github.com/DanikArduino/MathX',
    description='Extended math library for Python',
    long_description=open('README.md').read(),
    long_description_content_type = 'text/markdown',
    packages=find_packages(),
    pyton_requires='>=3.7',
    install_requires=[],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)