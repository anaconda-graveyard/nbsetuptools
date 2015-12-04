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
python install.py --prefix $CONDA_ENV_PATH
```
