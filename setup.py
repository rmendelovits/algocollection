import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algocollection", # Replace with your own username
    version="0.0.2",
    author="Raymond Mendelovits",
    author_email="raymondmendelovits@gmail.com",
    description="An algorithm collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rmendelovits/algocollection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
