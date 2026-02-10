from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_map = defaultdict(list)
        for path_info in paths:
            parts = path_info.split(" ")
            directory = parts[0]
            
            for file_info in parts[1:]:
                idx = file_info.find('(')
                file_name = file_info[:idx]
                content = file_info[idx + 1 : -1]
    
                full_path = f"{directory}/{file_name}"
                content_map[content].append(full_path)
        
        return [group for group in content_map.values() if len(group) > 1]