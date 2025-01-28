/**
 * @param {number[][]} grid
 * @return {number}
 */
var gridGame = function(grid) {
    let forwardSumArray = [];
    let runningCount = 0;
    for(const num of grid[0])
    {
        runningCount += num;
        forwardSumArray.push(runningCount);
    }
    let totalSumTop = runningCount;

    let backwardSumArray = [];
    let totalSum = 0;
    for(const num of grid[1])
    {
        totalSum += num;
    }
    runningCount = 0;
    let totalSumButton = totalSum;

    for(const num of grid[1])
    {
        backwardSumArray.push(totalSum);
        totalSum -= num;
    }

    let maxFirstRobot = 0;
    let dropLocation = 0;
    for(let i = 0; i < forwardSumArray.length; i++)
    {
        let sumAtLocation = forwardSumArray[i] + backwardSumArray[i];
        if(sumAtLocation > maxFirstRobot)
        {
            maxFirstRobot = sumAtLocation;
            dropLocation = i;
        }
    }

    let maxTop = 0;
    for(let i = dropLocation + 1; i < grid[0].length; i++)
    {
        maxTop += grid[0][i];
    }

    let maxBottom = 0;
    for(let i = 0; i < dropLocation; i++)
    {
        maxBottom += grid[1][i];
    }

    if(maxTop > maxBottom)
    {
        return maxTop;
    }
    else
    {
        return maxBottom;
    }
};

let testCases = [ [ [[2,5,4],[1,5,1]], 4], [ [[3,3,1],[8,5,2]], 4], [ [[1,3,1,15],[1,3,3,1]], 7], [ ]]
for(let test of testCases)
{
    console.log('Input: ' + test[0] + '\nExpected output: ' + test[1] + '\nActual output: ' + gridGame(test[0]) + '\n');
}