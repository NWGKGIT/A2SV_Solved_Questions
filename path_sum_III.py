from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            
            num_paths = prefix_sums[current_sum - targetSum]
            
            prefix_sums[current_sum] += 1
            
            num_paths += dfs(node.left, current_sum)
            num_paths += dfs(node.right, current_sum)
            
            prefix_sums[current_sum] -= 1
            
            return num_paths
            
        return dfs(root, 0)