import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trajectory-donsheehy",
    version="0.0.1",
    author="Don Sheehy",
    author_email="don.r.sheehy@gmail.com",
    description="load and manipulate trajectory data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/donsheehy/geomcps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
