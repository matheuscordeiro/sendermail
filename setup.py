import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sendermail",
    version="0.0.1",
    author="Matheus Cordeiro de Melo",
    author_email="matheuscordeiro.melo@gmail.com",
    description="It sends mail in compatible formats with Mail Services using templates of Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheuscordeiro/sendermail",
    packages=["sendermail"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 3.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
