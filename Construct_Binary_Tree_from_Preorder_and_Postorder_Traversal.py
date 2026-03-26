class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        left_size = postorder.index(preorder[1]) + 1
        
        root.left = self.constructFromPrePost(
            preorder[1 : left_size + 1], 
            postorder[:left_size]
        )
        root.right = self.constructFromPrePost(
            preorder[left_size + 1 :], 
            postorder[left_size : -1]
        )
        
        return root
    
    
# i did't get it, I just memorized it