from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data  # 현재 노드를 상징하는 값
        self.count = 0  # 현재 노드가 소유한 모든 자식 노드의 숫자
        self.child = {}  # 현재 노드의 자식 노드(dict)


class Trie:
    def __init__(self):
        self.head = Node(None)  # 최상위 노드를 생성

    def insert(self, string):
        cur = self.head  # 최상위 노드를 불러옴
        cur.count += 1

        for c in string:  # 한 글자씩
            if c not in cur.child:  # c가 cur.child에 없다면
                cur.child[c] = Node(c)  # child[c]에 자식노드(c)를 생성
            cur = cur.child[c]  # cur.child[c]가 cur을 대체
            cur.count += 1  # cur을 대체하게 된 cur.child[c]의 count를 +1

    def count(self, prefix):
        cur = self.head  # 최상위 노드를 불러옴

        for c in prefix:  # 입력받은 단어를 한 글자씩 c에 넣고 반복
            if c not in cur.child:  # c가 cur.child에 없으면
                return 0  # 0을 반환
            cur = cur.child[c]  # 있다면 자식노드로 이동

        return cur.count  # 최종적으로 자식노드에 도착했다면 cur.count를 반환


def solution(words, queries):
    answer = []
    tries = create_trie(words)  # Trie를 생성
    reversed_tries = create_trie(words, True)  # Trie를 거꾸로 생성

    for query in queries:
        answer.append(count_matched_word(tries, reversed_tries, query))

    return answer


def create_trie(words, is_reversed=False):
    trie_dic = defaultdict(Trie)  # dict를 생성할 시 기본적으로 Trie로 생성

    for word in words:
        if is_reversed:  # True일 경우, word를 뒤집는다
            word = word[::-1]
        trie_dic[len(word)].insert(word)  # trie_dict[word의 길이]에 word를 insert한다

    return trie_dic


def count_matched_word(tries, reversed_tries, query):
    no_mark_query = query.replace('?', '')  # 문자열 query 중에 모든 '?'를 ''로 바꿔줌

    if query[0] == '?':  # 첫 문자가 ?일 경우
        return reversed_tries[len(query)].count(no_mark_query[::-1])
    else:  # trie[query의 길이].count()
        return tries[len(query)].count(no_mark_query)


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
