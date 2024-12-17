/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean[]}
 */

let isArraySpecial = function(nums, queries) 
{
    let failNums = [];
    for(let i = 0; i < nums.length; i++)
    {
        if(i !== nums.length - 1 && nums[i] % 2 === nums[i+1] % 2)
        {
            failNums.push(i);
        }
    }

    let results = [];
    for(let i = 0; i < queries.length; i++)
    {
        if(checkQuery(failNums, queries[i]) === true)
        {
            results.push(true);
        }
        else
        {
            results.push(false);
        }
    }

    return results;
};

/**
 * @param {number[]} failIndexes 
 * @param {number[]} query 
 * @return {boolean}
 */
let checkQuery = function(failIndexes, query)
{
    let left = 0;
    let right = failIndexes.length - 1;
    while(true)
    {
        let mid = Math.floor(left + ((right - left) / 2));

        if(failIndexes[mid] >= query[0] && failIndexes[mid] < query[1])
        {
            return false;
        }
        else if(left > right)
        {
            return true;
        }
        else if(failIndexes[mid] < query[0])
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
};

let testCases = [ [[9,8,7,1,5,9], [[2,3]], false], [[3,4,1,2,6], [[0,4]], [false]], [[4,3,1,6], [[0,2],[2,3]], [false, true]] ];

for(let i = 0; i < testCases.length; i++)
{
    console.log('Input: ' + testCases[i][0] + ', ' + testCases[i][1] + '\nExpected output: ' + testCases[i][2] + '\nActual output: ' + isArraySpecial(testCases[i][0], testCases[i][1]) + '\n');
}