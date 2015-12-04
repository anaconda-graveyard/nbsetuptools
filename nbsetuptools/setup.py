import setuptools


setuptools.setup(
    name="nbsetuptools",
    version='0.1.0',
    url="https://github.com/anaconda-server/anaconda-notebook",
    author="Continuum Analytics",
    author_email="info@continuum.io",
    description="Help you install your nbextensions",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=["funcsigs", "notebook"]
)
