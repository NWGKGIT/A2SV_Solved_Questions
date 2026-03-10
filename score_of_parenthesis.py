class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                last = stack.pop()

                val = max(2 * last, 1)
                stack[-1] += val
        return stack[0]
# very tricky, you must revist later!!