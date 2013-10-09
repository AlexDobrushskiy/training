#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

import unittest
from raws import *
from random import choice


class Task1Test(unittest.TestCase):
    def setUp(self):
        self.elements = ["", "a", "", "b", "", "c"]

    def test_long_list_input(self):
        input = [choice(self.elements) for i in range(10000)]
        result = proccess_raws(input)

        previous = ""
        for i in result:
            if i == "":
                self.assertNotEqual(previous, "")
            previous = i

    def test_generator_input(self):
        def input_generator():
            for i in range(10000):
                yield choice(self.elements)

        result = proccess_raws(input_generator())

        previous = ""
        for i in result:
            if i == "":
                self.assertNotEqual(previous, "")
            previous = i


if __name__ == '__main__':
    unittest.main()
