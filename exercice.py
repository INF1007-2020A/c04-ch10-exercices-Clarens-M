#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64)

def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(co[0]**2 + co[1]**2), np.arctan(co[1], co[0])) for co in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values-number).argmin()

def exo4():
    valeurs = np.linspace(-1, 1, 250)
    a = np.array([x, x**2 * np.sin(1/(x**2)) + x] for x in valeurs)
    return a

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
#    print(coordinate_conversion(np.array([])))


    pass
