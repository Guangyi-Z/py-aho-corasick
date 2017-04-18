#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_py_aho_corasick
----------------------------------

Tests for `py_aho_corasick` module.
"""

import pytest


from py_aho_corasick import py_aho_corasick


def test_keywords_only():
    py_aho_corasick.init_trie(['cash', 'shew', 'ew'])
    text = "cashew"
    keywords = py_aho_corasick.get_keywords_found(text)
    for idx,k,v in keywords:
        assert text[idx:idx+len(k)] == k
    assert len(keywords) == 3


def test_keywords_and_values():
    kv = [('cash',1), ('shew',2), ('ew',3)]
    kv_dict = dict(kv)
    py_aho_corasick.init_trie(kv)
    text = "cashew"
    keywords = py_aho_corasick.get_keywords_found(text)
    for idx,k,v in keywords:
        assert text[idx:idx+len(k)] == k
        assert v == kv_dict[k]
    assert len(keywords) == 3


def test_unicode():
    kv = [(u'哈哈',1), (u'你好',2), (u'算我shu',3)]
    kv_dict = dict(kv)
    py_aho_corasick.init_trie(kv)
    text = u'你好哈哈算我shu咯'
    keywords = py_aho_corasick.get_keywords_found(text)
    for idx,k,v in keywords:
        assert text[idx:idx+len(k)] == k
        assert v == kv_dict[k]
    assert len(keywords) == 3


def test_utf8():
    kv = [(u'哈哈'.encode('utf8'),1), (u'你好'.encode('utf8'),2), (u'算我shu'.encode('utf8'),3)]
    kv_dict = dict(kv)
    py_aho_corasick.init_trie(kv)
    text = u'你好哈哈算我shu咯'.encode('utf8')
    keywords = py_aho_corasick.get_keywords_found(text)
    for idx,k,v in keywords:
        assert text[idx:idx+len(k)] == k
        assert v == kv_dict[k]
    assert len(keywords) == 3
