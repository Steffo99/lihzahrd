import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="lihzahrd",
    version="1.0b5",
    author="Stefano Pigozzi",
    author_email="ste.pigozzi@gmail.com",
    description="A Terraria world parser in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Steffo99/lihzahrd",
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7"
    ],
    include_package_data=True,
    zip_safe=False,
)
