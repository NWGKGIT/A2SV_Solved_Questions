class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total_sum = 0
        
        def dfs(node, p_val, gp_val):
            if not node:
                return
            
            if gp_val is not None and gp_val % 2 == 0:
                self.total_sum += node.val
            
            dfs(node.left, node.val, p_val)
            dfs(node.right, node.val, p_val)
            
        dfs(root, None, None)
        return self.total_sum