#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

import unittest
from raws import *
from random import choice


class Task1Test(unittest.TestCase):
    def setUp(self):
        self.input_list = ["", "", "", "a", "b", "", "", "c", "", "d", "", "", ""]

    def test_sanity(self):
        result = proccess_raws(self.input_list)
        self.assertEqual(result, ["a", "b", "", "c", "", "d"])

    def test_long_list(self):
        elements = ["", "a", "", "b", "", "c"]
        input = [choice(elements) for i in range(10000)]
        result = proccess_raws(input)
        self.assertNotEqual(result[0], "")
        self.assertNotEqual(result[-1], "")
        for i in range(len(result)):
            if result[i] == "":
                self.assertNotEqual(result[i-1], "")
                self.assertNotEqual(result[i+1], "")


if __name__ == '__main__':
    unittest.main()
