# -*- coding: utf-8 -*-

from collections import deque


AdjList = None


def init_trie(keywords):
    """ creates a trie of keywords, then sets fail transitions """
    create_empty_trie()
    if isinstance(keywords[0], tuple):
        add_keywords_and_values(keywords)
    else:
        add_keywords(keywords)
    set_fail_transitions()


def create_empty_trie():
    """ initalize the root of the trie """
    global AdjList
    AdjList = list()
    AdjList.append({'value':'', 'next_states':[],'fail_state':0,'output':[]})


def add_keywords(keywords):
    """ add all keywords in list of keywords """
    for keyword in keywords:
        add_keyword(keyword, None)


def add_keywords_and_values(kvs):
    """ add all keywords and values in list of (k,v) """
    for k,v in kvs:
        add_keyword(k,v)


def find_next_state(current_state, value):
    for node in AdjList[current_state]["next_states"]:
        if AdjList[node]["value"] == value:
            return node
    return None


def add_keyword(keyword, value):
    """ add a keyword to the trie and mark output at the last node """
    current_state = 0
    j = 0
    keyword = keyword.lower()
    child = find_next_state(current_state, keyword[j])
    while child != None:
        current_state = child
        j = j + 1
        if j < len(keyword):
            child = find_next_state(current_state, keyword[j])
        else:
            break
    for i in range(j, len(keyword)):
        node = {'value':keyword[i],'next_states':[],'fail_state':0,'output':[]}
        AdjList.append(node)
        AdjList[current_state]["next_states"].append(len(AdjList) - 1)
        current_state = len(AdjList) - 1
    AdjList[current_state]["output"].append((keyword,value))


def set_fail_transitions():
    q = deque()
    child = 0
    for node in AdjList[0]["next_states"]:
        q.append(node)
        AdjList[node]["fail_state"] = 0
    while q:
        r = q.popleft()
        for child in AdjList[r]["next_states"]:
            q.append(child)
            state = AdjList[r]["fail_state"]
            while find_next_state(state, AdjList[child]["value"]) == None and state != 0:
                state = AdjList[state]["fail_state"]
            AdjList[child]["fail_state"] = find_next_state(state, AdjList[child]["value"])
            if AdjList[child]["fail_state"] is None:
                AdjList[child]["fail_state"] = 0
            AdjList[child]["output"] = AdjList[child]["output"] + AdjList[AdjList[child]["fail_state"]]["output"]


def get_keywords_found(line):
    """ returns true if line contains any keywords in trie, format: (start_idx,kw,value) """
    line = line.lower()
    current_state = 0
    keywords_found = []

    for i in range(len(line)):
        while find_next_state(current_state, line[i]) is None and current_state != 0:
            current_state = AdjList[current_state]["fail_state"]
        current_state = find_next_state(current_state, line[i])
        if current_state is None:
            current_state = 0
        else:
            for k,v in AdjList[current_state]["output"]:
                keywords_found.append((i-len(k) + 1, k, v))

    return keywords_found


if __name__ == '__main__':
    init_trie(['cash', 'shew', 'ew'])
    for idx,st in enumerate(AdjList):
        print(idx, st)
    print('')
    for pair in get_keywords_found("cashew"):
        print(pair)
