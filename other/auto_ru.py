#! /env/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

"""
This module is attempt to parse catalog.auto.ru - cars brand and models catalog.
The purpose of pasing is to get brands dictionary with brand as a key and list of
brand's models as value.
{"toyota": ["avalon", "avensis","brevia", ...]}
"""

import urllib
import lxml.html


def get_auto_dict():
    page = urllib.urlopen('http://catalog.auto.ru/')

    doc = lxml.html.document_fromstring(page.read())

    table = doc.xpath('/html/body/div[1]/div[2]/article/div/table/tr/td[2]/div[2]/div[2]/div[2]/div/table')[0]

    brands = {}
    for i in table.getchildren():
        for j in i.getchildren():
            if j.text_content() != '&nbsp':
                brand = j.text_content()
                link = "http://catalog.auto.ru" + j.getchildren()[0].getchildren()[0].values()[0]
                brands[brand] = link

    result = {}


    for b in brands:
        page = urllib.urlopen(brands[b])
        doc = lxml.html.document_fromstring(page.read())
        table = doc.xpath('/html/body/div[1]/div[2]/article/div/table/tr/td[2]/div[2]/div[3]/div[1]/table')[0]

        result[b] = []
        for i in table.getchildren():
            for j in i.getchildren():
                if j.text_content() != '&nbsp':
                    model = j.text_content()
                    result[b].append(model)

    return result