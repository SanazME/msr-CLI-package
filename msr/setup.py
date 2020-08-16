import setuptools
from msr._version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = ['requests']

setuptools.setup(
    name="msr", 
    version=__version__,
    author="Sanaz Esf",
    author_email="sanaz.azh@gmail.com",
    description="A CLI package that performs various measurements on remote web page",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanazME/msr-CLI-package",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'msr =  msr.msrCommands:main'
        ]
    },
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='cli webpage measurement'
)