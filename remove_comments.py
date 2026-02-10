class Solution:
    def removeComments(self,source):
        res = []
        buffer = []
        in_block = False
        
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                next_char = line[i+1] if i + 1 < len(line) else ""
                if not in_block:
                    if char == '/' and next_char == '*':
                        in_block = True
                        i += 1
                    elif char == '/' and next_char == '/':
                        break 
                    else:
                        buffer.append(char)
                else:
                    if char == '*' and next_char == '/':
                        in_block = False
                        i += 1 
                i += 1
            
            if not in_block and buffer:
                res.append("".join(buffer))
                buffer = [] 
        return res