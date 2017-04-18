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
* The prototype is inspired by and borrowed from [Carolyn Shen](http://carshen.github.io/data-structures/algorithms/2014/04/07/aho-corasick-implementation-in-python.html)

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

Compared with [pyahocorasick](https://github.com/WojciechMula/pyahocorasick).

You can run the testing script to get this:

```bash
python cmp.py
```

* pyahocorasick: text of 1000000 length, 1000 keywords, and searching time cost 0.06532979011535645
* py_aho_corasick: text of 1000000 length, 1000 keywords, and searching time cost 4.912902116775513

TODO
--------

* <keyword,value> pairs
* Unicode support
* py2 && py3 support
* Pickle test
