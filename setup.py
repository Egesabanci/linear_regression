import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linreg",
    version="0.1",
    author="Ege Sabancı",
    author_email="egesabanci@outlook.com.tr",
    description="Linear Regression algorithm module for regression problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Egesabanci/linreg",
    download_url = "https://pypi.org/project/linreg",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "matplotlib", "statistics"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)