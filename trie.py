class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

    def insert(self, word: str):
        cur = self
        for char in word:
            if char not in cur.child:
                cur.child[char] = TrieNode()
            cur = cur.child[char]
        cur.end = True

    def search(self, word: str):
        cur = self
        for char in word:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        return cur.end


if __name__ == "__main__":
    t = TrieNode()
    t.insert("haha")
    t.insert("哈哈")
    print(t.search("ha"), t.search("haha"), t.search("哈"), t.search("哈哈"))
