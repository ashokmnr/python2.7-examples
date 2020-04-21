from setuptools import setup, find_packages

with open("README.rst") as f:
    readme = f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    description="Database backups locally or to AWS S3.",
    long_description=readme,
    author="Ashok Thakur",
    author_email="ashokmnr160@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[]
)