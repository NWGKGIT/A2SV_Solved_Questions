from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charmap=Counter(chars)
        ans=0
        for word in words:
            wcount=Counter(word)
            for k,v in wcount.items():
                if charmap[k]<v:
                    break
            else:
                ans+=len(word)
        return ans