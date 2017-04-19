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
    NW = 50000
    for i in range(NW):
        nw = random.randint(5,10)
        kw = rand_str(nw)
        keywords.append(kw)

    # pyahocorasick
    start_t = time.time()
    A = ahocorasick.Automaton()
    for idx, key in enumerate(keywords):
        A.add_word(key, (idx, key))
    A.make_automaton()
    delta_build1 = time.time() - start_t

    start_t = time.time()
    cnt1 = 0
    for end_index, (insert_order, original_value) in A.iter(text):
        start_index = end_index - len(original_value) + 1
        assert text[start_index:start_index + len(original_value)] == original_value
        cnt1 += 1
    delta_search1 = time.time() - start_t

    # py_aho_corasick
    start_t = time.time()
    A = py_aho_corasick.Automaton(keywords)
    delta_build2 = time.time() - start_t

    start_t = time.time()
    kv = A.get_keywords_found(text)
    cnt2 = 0
    for idx,k,v in kv:
        assert text[idx:idx+len(k)] == k
        cnt2 += 1
    delta_search2 = time.time() - start_t

    # brute force
    start_t = time.time()
    cnt3 = 0
    for kw in keywords:
        beg = 0
        while beg < len(text):
            idx = text.find(kw, beg)
            if idx == -1:
                break
            else:
                assert text[idx:idx+len(kw)] == kw
                beg = idx + 1
                cnt3 += 1
    delta_search3 = time.time() - start_t

    print(cnt1)
    assert cnt1 == cnt2
    assert cnt1 == cnt3

    # output
    print('pyahocorasick: text of {0} length, {1} keywords, building time {2} and searching time cost {3}'.format(N,NW,delta_build1,delta_search1))
    print('py_aho_corasick: text of {0} length, {1} keywords, building time {2} and searching time cost {3}'.format(N,NW,delta_build2,delta_search2))
    print('brute force: text of {0} length, {1} keywords, building time {2} and searching time cost {3}'.format(N,NW,0,delta_search3))
