class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        dict2 = {}
        for j in range(len(list2)):
            dict2[list2[j]] = j
        mini = float("inf")
        results = []
        for i in range(len(list1)):
            if list1[i] in dict2:
                curr = dict2[list1[i]] + i
                if curr < mini:
                    mini = curr
                    results = [list1[i]]
                elif curr == mini:
                    results.append(list1[i])
        return results
