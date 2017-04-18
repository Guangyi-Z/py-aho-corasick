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

* Aho-Corasick's Trie structure and Failure State Transition
* String searching algorithm for multi-pattern keywords
* Pure Python implementation

Usage
--------

TODO

Performance
--------

Compared with `pyahocorasick <https://github.com/WojciechMula/pyahocorasick>`_

You can run the testing script to get this:

    # Requirements:
    # pip install pyahocorasick
    python cmp.py

* pyahocorasick: text of 1000000 length, 1000 keywords, building time 0.026426076889038086 and searching time cost 0.047805070877075195
* py_aho_corasick: text of 1000000 length, 1000 keywords, building time 0.47435593605041504 and searching time cost 4.24287486076355

TODO
--------

* Unicode support
* py2 && py3 support
* Pickle test
