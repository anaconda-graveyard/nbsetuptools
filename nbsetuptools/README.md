# NBSetupTools

> Help you install your nbextensions

## How to use

``` python
import nbsetuptools

nbsetuptools.setup(
    join(abspath(dirname(__file__)), 'static'),
    name='hello_world',
    version='0.1.0'
)
```

Later you can run:

```
python setup.py install --prefix $CONDA_ENV_PATH
python setup.py remove --prefix $CONDA_ENV_PATH
```
