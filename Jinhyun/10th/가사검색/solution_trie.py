from collections import defaultdict

class Node() :
    def __init__(self, key, passnumber = None) :
        self.key = key
        self.passnumber = defaultdict(int) # length값 저장 위한 dict
        self.children = {}

class Trie() :
    def __init__(self) :
        self.head = Node(None)

    def insert(self, string) :
        curr_node = self.head # 노드 시작
        string_len = len(string)
        curr_node.passnumber[string_len] += 1 # 현재 node의 
        for char in string :
            if char not in curr_node.children :
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            curr_node.passnumber[string_len] += 1 # 해당 노드 지나가는 string길이가 string_len인 것의 개수 저장

    def search(self, query) :
        curr_node = self.head
        for q in query :
            # 앞 뒤 둘다 '?' 인 경우에도 어차피 막힌다.
            if q == '?' :
                break
            if q in curr_node.children :
                curr_node = curr_node.children[q]
            else :
                return 0
        return curr_node.passnumber[len(query)]

def solution_trie(words, queries) :
    trie = Trie()
    reverse_trie = Trie()
    answer = []
    for i in range(len(words)) :
        trie.insert(words[i])
        reverse_trie.insert(words[i][::-1])
    for query in queries :
        if query.endswith('?') : # endswith : 접미사가 해당 원소일 경우 True 반환
            result = trie.search(query)
            answer.append(result)
        else :
            result = reverse_trie.search(query[::-1])
            answer.append(result)
    return answer

print(solution_trie(['frodo','front','frost','frozen','frame','kakao'],['fro??','????o','fr???','fro???','pro?']))