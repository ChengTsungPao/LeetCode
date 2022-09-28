/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

typedef TreeNode* TreeNodePtr;

class Solution {
public:
    TreeNode* ans = nullptr;
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(p -> val > q -> val){
            swap(p, q);
        }
        recur(root, p, q);
        return ans;
    }

    int recur(TreeNode* root, TreeNode* p, TreeNode* q){
        if(!root){
            return 0;
        }
        
        int hitCount = 0;        
        if(root -> val == p -> val or root -> val == q -> val){
            hitCount += 1;
        }
        
        hitCount += (root -> val > p -> val) ? recur(root -> left, p, q) : 0;
        hitCount += (root -> val < q -> val) ? recur(root -> right, p, q) : 0;

        if(hitCount == 2 && !ans){
            ans = root;
        }
        
        return hitCount;
    }
    
    void swap(TreeNodePtr &a, TreeNodePtr &b){
        TreeNode* temp = a;
        a = b;
        b = temp;
    }
};