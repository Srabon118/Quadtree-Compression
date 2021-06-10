"""
Assignment 2: Quadtree Compression

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the test suite
"""

import pytest
from a2tree import QuadTree

"""
Test cases
"""


def test_split_quadrants_1():
    example = QuadTree(0)
    quadrants = example._split_quadrants(
        [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30]
        ]
    )

    assert quadrants == [
        [[1, 2, 3],
         [7, 8, 9]],

        [[4, 5, 6],
         [10, 11, 12]],

        [[13, 14, 15],
         [19, 20, 21],
         [25, 26, 27]],

        [[16, 17, 18],
         [22, 23, 24],
         [28, 29, 30]]
    ]


def test_split_quadrants_2():
    example = QuadTree(0)
    quadrants = example._split_quadrants(
        [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24]
        ]
    )

    assert quadrants == [
        [[1, 2, 3],
         [7, 8, 9]],

        [[4, 5, 6],
         [10, 11, 12]],

        [[13, 14, 15],
         [19, 20, 21]],

        [[16, 17, 18],
         [22, 23, 24]]
    ]


def test_split_quadrants_3():
    example = QuadTree(0)
    quadrants = example._split_quadrants([[0]])

    assert quadrants == [
        [],

        [],

        [[]],

        [[0]]
    ]


def test_split_quadrants_4():
    example = QuadTree(0)
    quadrants = example._split_quadrants(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    )

    assert quadrants == [
        [[1, 2],
         [6, 7]],

        [[3, 4, 5],
         [8, 9, 10]],

        [[11, 12],
         [16, 17],
         [21, 22]],

        [[13, 14, 15],
         [18, 19, 20],
         [23, 24, 25]]
    ]


def test_restore_from_preorder_1():
    example = QuadTree(0)
    pixels = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30]
    ]
    example.build_quad_tree(pixels)
    preorder_list = [i for i in example.preorder().split(",")]

    check = QuadTree(0)
    check = check.restore_from_preorder(preorder_list, len(pixels[0]), len(pixels))
    check_pixels = check.convert_to_pixels()

    assert pixels == check_pixels


def test_restore_from_preorder_2():
    example = QuadTree(0)
    pixels = [
            [11, 12, 13, 14, 15, 61],
            [16, 17, 18, 19, 20, 12],
            [21, 22, 23, 24, 25, 62],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [11, 12, 13, 14, 15, 61],
            [16, 17, 18, 19, 20, 12],
            [21, 22, 23, 24, 25, 62],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30]
        ]
    example.build_quad_tree(pixels)
    preorder_list = [i for i in example.preorder().split(",")]

    check = QuadTree(0)
    check = check.restore_from_preorder(preorder_list, len(pixels[0]), len(pixels))
    check_pixels = check.convert_to_pixels()

    assert pixels == check_pixels


def test_restore_from_preorder_3():
    example = QuadTree(0)
    pixels = [
        [1, 4],
        [2, 6]
    ]
    example.build_quad_tree(pixels)
    preorder_list = [i for i in example.preorder().split(",")]

    check = QuadTree(0)
    check = check.restore_from_preorder(preorder_list, len(pixels[0]), len(pixels))
    check_pixels = check.convert_to_pixels()

    assert pixels == check_pixels


def test_restore_from_preorder_4():
    example = QuadTree(0)
    pixels = [
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    ]
    example.build_quad_tree(pixels)
    preorder_list = [i for i in example.preorder().split(",")]

    check = QuadTree(0)
    check = check.restore_from_preorder(preorder_list, len(pixels[0]), len(pixels))
    check_pixels = check.convert_to_pixels()

    assert pixels == check_pixels


if __name__ == '__main__':

    pytest.main(['a2test_student.py'])
