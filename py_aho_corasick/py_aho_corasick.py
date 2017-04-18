# -*- coding: utf-8 -*-

from collections import deque


class Automaton(object):

    def __init__(self, keywords):
        """ creates a trie of keywords, then sets fail transitions """

        # initalize the root of the trie
        self.AdjList = list()
        self.AdjList.append({'value':'', 'next_states':[],'fail_state':0,'output':[]})

        if isinstance(keywords[0], tuple):
            self.add_keywords_and_values(keywords)
        else:
            self.add_keywords(keywords)
        self.set_fail_transitions()

    def add_keywords(self, keywords):
        """ add all keywords in list of keywords """
        for keyword in keywords:
            self.add_keyword(keyword, None)

    def add_keywords_and_values(self, kvs):
        """ add all keywords and values in list of (k,v) """
        for k,v in kvs:
            self.add_keyword(k,v)

    def find_next_state(self, current_state, value):
        for node in self.AdjList[current_state]["next_states"]:
            if self.AdjList[node]["value"] == value:
                return node
        return None

    def add_keyword(self, keyword, value):
        """ add a keyword to the trie and mark output at the last node """
        current_state = 0
        j = 0
        keyword = keyword.lower()
        child = self.find_next_state(current_state, keyword[j])
        while child != None:
            current_state = child
            j = j + 1
            if j < len(keyword):
                child = self.find_next_state(current_state, keyword[j])
            else:
                break
        for i in range(j, len(keyword)):
            node = {'value':keyword[i],'next_states':[],'fail_state':0,'output':[]}
            self.AdjList.append(node)
            self.AdjList[current_state]["next_states"].append(len(self.AdjList) - 1)
            current_state = len(self.AdjList) - 1
        self.AdjList[current_state]["output"].append((keyword,value))

    def set_fail_transitions(self):
        q = deque()
        child = 0
        for node in self.AdjList[0]["next_states"]:
            q.append(node)
            self.AdjList[node]["fail_state"] = 0
        while q:
            r = q.popleft()
            for child in self.AdjList[r]["next_states"]:
                q.append(child)
                state = self.AdjList[r]["fail_state"]
                while self.find_next_state(state, self.AdjList[child]["value"]) == None and state != 0:
                    state = self.AdjList[state]["fail_state"]
                self.AdjList[child]["fail_state"] = self.find_next_state(state, self.AdjList[child]["value"])
                if self.AdjList[child]["fail_state"] is None:
                    self.AdjList[child]["fail_state"] = 0
                self.AdjList[child]["output"] = self.AdjList[child]["output"] + self.AdjList[self.AdjList[child]["fail_state"]]["output"]

    def get_keywords_found(self, line):
        """ returns true if line contains any keywords in trie, format: (start_idx,kw,value) """
        line = line.lower()
        current_state = 0
        keywords_found = []

        for i in range(len(line)):
            while self.find_next_state(current_state, line[i]) is None and current_state != 0:
                current_state = self.AdjList[current_state]["fail_state"]
            current_state = self.find_next_state(current_state, line[i])
            if current_state is None:
                current_state = 0
            else:
                for k,v in self.AdjList[current_state]["output"]:
                    keywords_found.append((i-len(k) + 1, k, v))

        return keywords_found


if __name__ == '__main__':
    A = Automaton(['cash', 'shew', 'ew'])
    for idx,st in enumerate(A.AdjList):
        print(idx, st)
    print('')
    for pair in A.get_keywords_found("cashew"):
        print(pair)
