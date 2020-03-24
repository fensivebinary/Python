import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terminalchart", # Replace with your own username
    version="1.0.0",
    author="Muhammad Junaid Raza",
    author_email="strawberriesfrozen@gmail.com",
    description="Make chart on commanline interface.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frozenstrawberries/Python/tree/master/terminalchart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)