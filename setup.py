from distutils.core import setup


setup(
    name="nbsetuptools",
    version='0.1.4',
    url="https://github.com/anaconda-server/nbsetuptools",
    author="Continuum Analytics",
    author_email="info@continuum.io",
    description="Help you install your nbextensions",
    packages=['nbsetuptools'],
    license='BSD',
    install_requires=[
        'funcsigs',
        'jupyter'
    ]
)
