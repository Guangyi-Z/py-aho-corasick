#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_py_aho_corasick
----------------------------------

Tests for `py_aho_corasick` module.
"""

import pytest


from py_aho_corasick import py_aho_corasick


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    py_aho_corasick.init_trie(['cash', 'shew', 'ew'])
    text = "cashew"
    keywords = py_aho_corasick.get_keywords_found(text)
    for idx,k,v in keywords:
        assert text[idx:idx+len(k)] == k
    assert len(keywords) == 3
