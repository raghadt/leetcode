class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1)!=len(words2):
            return False
        
        pairset = set(map(tuple, pairs))
        return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset
           for w1, w2 in zip(words1, words2))