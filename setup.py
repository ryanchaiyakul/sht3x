import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sht3x",
    version="0.0.5",
    author="Ryan Chaiyakul",
    description="Sht3x python driver for stickytoe framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryanchaiyakul/sht3x",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['smbus2 >= 0.3.0',
                      'stickytoe-device >= 0.0.1',
                      ],
)
