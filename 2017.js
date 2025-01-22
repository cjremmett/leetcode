/**
 * @param {number[][]} grid
 * @return {number}
 */
var gridGame = function(grid) {
    return 5;
};

let testCases = [ [ [[2,5,4],[1,5,1]], 4], [ [[3,3,1],[8,5,2]], 4], [ [[1,3,1,15],[1,3,3,1]], 7]]
for(let test of testCases)
{
    console.log('Input: ' + test[0] + '\nExpected output: ' + test[1] + '\nActual output: ' + gridGame(test[0]) + '\n');
}