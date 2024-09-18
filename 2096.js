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
    let startLevel
    let destLevel
    let nodeQueue = new Array()
    nodeQueue.push([root, 0])
    let depthLevel = 0
    while(nodeQueue.length > 0)
    {
        depthLevel = nodeQueue[0][1]
        if(nodeQueue[0][0].val === startValue)
        {
            startLevel = depthLevel
        }

        if(nodeQueue[0][0].val === destValue)
        {
            destLevel = depthLevel
        }

        if(nodeQueue[0][0].left != null)
        {
            nodeQueue.push(nodeQueue[0][0].left, depthLevel + 1)
        }

        if(nodeQueue[0][0].right != null)
        {
            nodeQueue.push(nodeQueue[0][0].right, depthLevel + 1)
        }

        nodeQueue.shift(0)
    }

    return [startLevel, destLevel]
};

node2 = new TreeNode(2, null, null)
node1 = new TreeNode(1, null, null)
nodeRoot = new TreeNode(3, node1, node2)
console.log(getDirections(nodeRoot, node1.val, node2.val))