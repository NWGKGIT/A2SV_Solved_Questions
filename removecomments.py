import re

class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        return [s for s in re.sub(r'//.*|/\*(?s:.*?)\*/', '', '\n'.join(source)).split('\n') if s]