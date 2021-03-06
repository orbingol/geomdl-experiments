"""
.. module:: letters
    :platform: Unix, Windows
    :synopsis: Letters of the alphabet

.. moduleauthor:: Onur Rauf Bingol <orbingol@gmail.com>

"""

from geomdl.shapes import curve2d
from geomdl import NURBS
from geomdl import Multi
from geomdl import utilities
from geomdl import operations


def letter_i():
    base = NURBS.Curve()
    base.degree = 3
    base.ctrlptsw = [[1, 20, 1], [0, 10, 0.5],
                     [0, 19, 1], [0, 10, 1], [0, 1, 1], [0, 0, 0.5],
                     [1, 0, 1], [1, 0, 0.5],
                     [2, 1, 1], [2, 10, 1], [2, 19, 1], [1, 10, 0.5], [1, 20, 1]]
    base.knotvector = utilities.generate_knot_vector(base.degree, len(base.ctrlpts))

    hat = curve2d.full_circle(radius=1)
    operations.translate(hat, (1, 22), inplace=True)

    letter = Multi.MultiCurve()
    letter.add([base, hat])

    return letter


def letter_o():
    outer = curve2d.full_circle(radius=10.0)
    operations.translate(outer, (2, 0), inplace=True)
    inner = curve2d.full_circle(radius=8.0)
    operations.translate(inner, (2, 0), inplace=True)

    letter = Multi.MultiCurve()
    letter.add([outer, inner])

    return letter
