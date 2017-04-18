# -*- coding: utf-8 -*-
'''
Performance Testing

Requirements:
pip install pyahocorasick
'''

import random
import string
import time
from py_aho_corasick import py_aho_corasick
import ahocorasick


rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])


if __name__ == '__main__':
    N = 1000000
    text = rand_str(N)

    keywords = list()
    NW = 1000
    for i in range(NW):
        nw = random.randint(30,100)
        kw = rand_str(nw)
        keywords.append(kw)

    # pyahocorasick
    start_t = time.time()
    A = ahocorasick.Automaton()
    for idx, key in enumerate(keywords):
        A.add_word(key, (idx, key))
    A.make_automaton()
    cnt1 = 0
    for end_index, (insert_order, original_value) in A.iter(text):
        start_index = end_index - len(original_value) + 1
        assert haystack[start_index:start_index + len(original_value)] == original_value
        cnt1 += 1
    delta1 = time.time() - start_t

    # py_aho_corasick
    start_t = time.time()
    py_aho_corasick.init_trie(keywords)
    keywords = py_aho_corasick.get_keywords_found(text)
    cnt2 = 0
    for idx,k,v in keywords:
        assert text[idx:idx+len(k)] == k
        cnt2 += 1
    delta2 = time.time() - start_t

    assert cnt1 == cnt2

    # output
    print('pyahocorasick: text of {0} length, {1} keywords, and searching time cost {2}'.format(N,NW,delta1))
    print('py_aho_corasick: text of {0} length, {1} keywords, and searching time cost {2}'.format(N,NW,delta2))
