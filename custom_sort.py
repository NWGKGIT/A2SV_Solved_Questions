class Solution:
    def customSortString(self, order: str, s: str) -> str:
        slist=list(s)

        def custom_sorter(x):
            if x in order:
                return order.index(x)
            else:
                return -1
        slist.sort(key=custom_sorter)
        return "".join(slist)