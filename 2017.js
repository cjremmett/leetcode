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

    let maxAtBestDropLocation = Number.MAX_SAFE_INTEGER;
    for(let i = 0; i < forwardSumArray.length; i++)
    {
        let topAtLocation = forwardSumArray[forwardSumArray.length -1] - forwardSumArray[i];
        let bottomAtLocation = backwardSumArray[0] - backwardSumArray[i];
        let mostAtLocation = 0;
        if(topAtLocation >= bottomAtLocation)
        {
            mostAtLocation = topAtLocation;
        }
        else
        {
            mostAtLocation = bottomAtLocation;
        }

        if(mostAtLocation < maxAtBestDropLocation)
        {
            maxAtBestDropLocation = mostAtLocation;
        }
    }

    return maxAtBestDropLocation;
};

let testCases = [ [ [[2,5,4],[1,5,1]], 4], [ [[3,3,1],[8,5,2]], 4], [ [[1,3,1,15],[1,3,3,1]], 7], [[[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]], 63]]
for(let test of testCases)
{
    console.log('Input: ' + test[0] + '\nExpected output: ' + test[1] + '\nActual output: ' + gridGame(test[0]) + '\n');
}
