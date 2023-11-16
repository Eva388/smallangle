# Smallange: calculating tan(x) or sin(x) for n amount of x values, where n is chosen in terminal
# 16-11-2023
# Eva Bredeweg

import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
# define function to make subcommands later
def groups():
    pass

@groups.command()
# give option to choose number that is argument in function sin
@click.option("-n", "--number", default = 1)
def sin(number):
    """Calculate sin(x) of x.

    Args:
        number (int): function creates this many values in the array

    Returns:
        dataframe: containing x and sin(x) values
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@groups.command()
# give option to choose number that is argument in function tan
@click.option("-n", "--number", default = 1)
def tan(number):
    """Calculate tan(x) of x.

    Args:
        number (int): function creates this many values in the array

    Returns:
        dataframe: containing x and tan(x) values
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

# give option to call smallange from anywhere
if __name__ == "__main__":
    groups()