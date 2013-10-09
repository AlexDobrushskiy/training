#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

__all__ = ('proccess_raws', )


def proccess_raws(input):
    """
    This functions receives a list of string as 'input' and processes them in the following way:
    Beginning and ending empty strings are eliminated, and sequences of empty strings at the middle of a list
     are compressed to one empty string.
    :param input: List of strings (may be a generator)
    :return: Generator object.
    """

    begin_flag = True
    empty_string_flag = False
    for item in input:
        if item:
            if begin_flag:
                begin_flag = False
            if empty_string_flag:
                yield ""
                empty_string_flag = False
            yield item
        else:
            if not begin_flag:
                empty_string_flag = True




