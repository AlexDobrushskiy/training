#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'


def proccess_raws(input):
    """
    This functions receives a list of string as 'input' and proccess them the following way:
    Beginning and ending empty strings eliminates, and sequences of empty strings at the middle of a list
     are compressed to one empty string.
    :param input: List of strings
    :return:
    """
    output = []
    begin_flag = True
    empty_string_flag = False
    for item in input:
        if item:
            if begin_flag:
                begin_flag = False
            if empty_string_flag:
                output.append("")
                empty_string_flag = False
            output.append(item)
        else:
            if not begin_flag:
                empty_string_flag = True

    return output



