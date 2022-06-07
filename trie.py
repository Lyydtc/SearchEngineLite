class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.tid = 0

    def insert(self, word: str, term_id=0):
        cur = self
        for char in word:
            if char not in cur.child:
                cur.child[char] = TrieNode()
            cur = cur.child[char]
        cur.end = True
        cur.tid = term_id

    def search(self, word: str):
        cur = self
        for char in word:
            if char not in cur.child:
                return False, 0
            cur = cur.child[char]
        return cur.end, cur.tid


if __name__ == "__main__":
    t = TrieNode()
    t.insert("haha")
    t.insert("哈哈")
    print(t.search("ha"), t.search("haha"), t.search("哈"), t.search("哈哈"))
