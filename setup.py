from distutils.core import setup


setup(
    name="nbsetuptools",
    version='0.1.0',
    url="https://github.com/anaconda-server/anaconda-notebook",
    author="Continuum Analytics",
    author_email="info@continuum.io",
    description="Help you install your nbextensions",
    long_description=open('README.md').read(),
    packages=['nbsetuptools'],
)