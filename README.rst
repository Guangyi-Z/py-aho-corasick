===============================
py-aho-corasick
===============================


.. image:: https://img.shields.io/pypi/v/py_aho_corasick.svg
        :target: https://pypi.python.org/pypi/py_aho_corasick

.. image:: https://img.shields.io/travis/JanFan/py_aho_corasick.svg
        :target: https://travis-ci.org/JanFan/py_aho_corasick

.. image:: https://readthedocs.org/projects/py-aho-corasick/badge/?version=latest
        :target: https://py-aho-corasick.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/JanFan/py_aho_corasick/shield.svg
     :target: https://pyup.io/repos/github/JanFan/py_aho_corasick/
     :alt: Updates


py-aho-corasick

* Free software: MIT license
* The prototype is inspired by and borrowed from `Carolyn Shen <http://carshen.github.io/data-structures/algorithms/2014/04/07/aho-corasick-implementation-in-python.html>`_

Features
--------

* Pure Python implementation
* Python2 && Python3 support
* Unicode && UTF-8 encoding support
* Pickle-able serialization

Background
--------

I re-invented this algorithm due to the need in my work.
I have checked other Aho-Corasick implementations for Python, but none of them meet my requirements.

* `pyahocorasick <https://github.com/WojciechMula/pyahocorasick>`_ by Wojciech Mula

 * Can't use unicode in Python 2.x.

* `noaho <https://github.com/JDonner/NoAho>`_ by Jeff Donner

 * No support for the pickle protocol.

* `acora <https://github.com/scoder/acora>`_ by Stefan Behnel

 * No support for a dict-like protocol to associate a value to a string key.

* `ahocorasick <https://hkn.eecs.berkeley.edu/~dyoo/python/ahocorasick/>`_ by Danny Yoo

 * I failed to build it as an egg distribution.

If you have the same issues like me, welcome abroad!

Usage
--------

Install::

    pip install py_aho_corasick

Usage::

    from py_aho_corasick import py_aho_corasick

    # keywords only
    A = py_aho_corasick.Automaton(['cash', 'shew', 'ew'])
    text = "cashew"
    for idx,k,v in A.get_keywords_found(text):
        assert text[idx:idx+len(k)] == k

    # keywords and values
    kv = [('cash',1), ('shew',2), ('ew',3)]
    A = py_aho_corasick.Automaton(kv)
    text = "cashew"
    for idx,k,v in A.get_keywords_found(text):
        assert text[idx:idx+len(k)] == k
        assert v == dict(kv)[k]


Performance
--------

Compared with `pyahocorasick (C extention) <https://github.com/WojciechMula/pyahocorasick>`_

You can run the testing script to get this::

    # Requirements:
    # pip install pyahocorasick
    python cmp.py

* pyahocorasick: text of 1000000 length, 1000 keywords, building time 0.026426076889038086 and searching time cost 0.047805070877075195
* py_aho_corasick: text of 1000000 length, 1000 keywords, building time 0.47435593605041504 and searching time cost 4.24287486076355

Sorry about the poor performance :-(

Development
--------

Run tests::

    # testing against py2 and py3
    tox


TODO
--------

* Performance optimization
