// Definition for a binary tree node.
function TreeNode(val, left, right) 
{
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @param {number} startValue
 * @param {number} destValue
 * @return {string}
 */
var getDirections = function(root, startValue, destValue) 
{
    nodeMap = new Map()
    nodeQueue = new Array()
    nodeQueue.push(root)
    while(nodeQueue.length > 0)
    {
        if(nodeQueue[0].left != null)
        {
            nodeMap.set(nodeQueue[0].left.val, nodeQueue[0].val)
            nodeQueue.push(nodeQueue[0].left)
        }

        if(nodeQueue[0].right != null)
        {
            nodeMap.set(nodeQueue[0].right.val, nodeQueue[0].val)
            nodeQueue.push(nodeQueue[0].right)
        }

        nodeQueue.shift()
    }
    
    startSeen = Set()
    destSeen = Set()
    commonAncestor = undefined

    
};

node2 = new TreeNode(2, null, null)
node1 = new TreeNode(1, null, null)
nodeRoot = new TreeNode(3, node1, node2)
console.log(getDirections(nodeRoot, node1.val, node2.val))