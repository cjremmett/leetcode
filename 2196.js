
function TreeNode(val, left, right) 
{
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) 
{
    const potentialRootSet = new Set()
    const nodeMap = new Map()
    descriptions.forEach((element) => {
        let newNode
        if(nodeMap.has(element[0]))
        {
            newNode = nodeMap.get(element[0])
        }
        else
        {
            newNode = new TreeNode(element[0])
            nodeMap.set(element[0], newNode)
            potentialRootSet.add(element[0])
        }

        if(nodeMap.has(element[1]))
        {
            const childNode = nodeMap.get(element[1])
            potentialRootSet.delete(element[1])
            if(element[2] === 0)
            {
                newNode.right = childNode
            }
            else
            {
                newNode.left = childNode
            }
        }
        else
        {
            const newChild = new TreeNode(element[1])
            nodeMap.set(element[1], newChild)
            if(element[2] === 0)
            {
                newNode.right = newChild
            }
            else
            {
                newNode.left = newChild
            }
        }
    })

    return nodeMap.get(Array.from(potentialRootSet)[0])
};


console.log(createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))
console.log(createBinaryTree([[1,2,1],[2,3,0],[3,4,1]]))