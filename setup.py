import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = ['requests']

setuptools.setup(
    name="msr-pkg", 
    version="1.0.0",
    author="Sanaz Esf",
    author_email="sanaz.azh@gmail.com",
    description="A CLI package that performs various measurements on remote web page",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanazME/msr-CLI-package",
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='cli webpage measurement'
)