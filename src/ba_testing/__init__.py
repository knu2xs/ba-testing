__title__ = 'ba-testing'
__version__ = '0.0.0'
__author__ = 'Esri Business Analyst Deveopment Team'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2021 by Esri Business Analyst Deveopment Team'

__all__ = ['example_function', 'ExampleObject']

# add specific imports below if you want to organize your code into modules, which is mostly what I do
## from . import utils

from typing import Union
from pathlib import Path

import pandas as pd


def example_function(in_path: Union[str, Path]) -> pd.DataFrame:
    """
    This is an example function, mostly to provide a template for properly
    structuring a function and docstring for both you, and also for myself,
    since I *almost always* have to look this up, and it's a *lot* easier
    for it to be already templated.

    Args:
        in_path: Required path to something you really care about, or at least
            want to exploit, a really big word used to simply say, *use*.

    Returns:
        Hypothetically, a Pandas Dataframe. Good luck with that.

    .. code-block:: python

        from ba_testing import example_function

        pth = r'C:/path/to/some/table.csv'

        df = example_function(pth)
    """
    return pd.read_csv(in_path)
