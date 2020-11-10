#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, num=64)

def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(co[0]**2 + co[1]**2), np.arctan(co[1], co[0])) for co in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values-number).argmin()

def exo4():
    x = np.linspace(-1, 1, num=250)
    y = x**2 * np.sin(1/(x**2)) + x

    plt.scatter(x, y)
    plt.show()

    return

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
#    print(linear_values())
#    print(coordinate_conversion(np.array([])))

    exo4()


    pass
