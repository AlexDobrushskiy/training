#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

import unittest
from raws import *


class Task1Test(unittest.TestCase):
    def setUp(self):
        self.input_list = ["", "", "", "a", "b", "", "", "c", "", "d", "", "", ""]

    def test_simple_case(self):
        result = proccess_raws(self.input_list)
        self.assertEqual(result, ["a", "b", "", "c", "", "d"])

