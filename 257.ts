// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


function binaryTreePaths(root: TreeNode | null): string[] {
    if(root == undefined)
    {
        console.log(`Passed undefined root node.`);
        return [];
    }
    else
    {
        let returnList: Array<string> = []
        traverseNode(root, [`${root.val}`], returnList);
        console.log(returnList);
        return returnList;
    }
};

function traverseNode(node: TreeNode, history: Array<string>, returnList: Array<string>): undefined {
    if(node.left == undefined && node.right == undefined)
    {
        for(let path of history)
        {
            console.log(`Pushing ${path}`);
            returnList.push(path);
        }
    }
    else
    {
        if(node.left != undefined)
        {   
            let newHistory = appendToHistory(node.left.val, history);
            traverseNode(node.left, newHistory, returnList);
        }

        if(node.right != undefined)
        {   
            let newHistory = appendToHistory(node.right.val, history);
            traverseNode(node.right, newHistory, returnList);
        }
    }
}

function appendToHistory(val: number, history: Array<string>): Array<string> {
    let returnHistory = new Array<string>;
    for(let path of history)
    {
        returnHistory.push(`${path}->${val}`)
    }
    return returnHistory;
}

let node5 = new TreeNode(5, undefined, undefined);
let node3 = new TreeNode(3, undefined, undefined);
let node2 = new TreeNode(2, undefined, node5);
let node1 = new TreeNode(1, node2, node3);
binaryTreePaths(node1);