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
        if(i === nums.length - 1)
        {
            failNums.push(true);
        }
        else if(nums[i] % 2 === nums[i+1] % 2)
        {
            failNums.push(true);
        }
        else
        {
            failNums.push(false);
        }
    }
};

let testCases = [ [[3,4,1,2,6], [[0,4]], [false]], [[4,3,1,6], [[0,2],[2,3]], [false, true]] ];

for(let i = 0; i < testCases.length; i++)
{
    console.log('Input: ' + testCases[i][0] + ', ' + testCases[i][1] + '\nExpected output: ' + testCases[i][2] + '\nActual output: ' + isArraySpecial(testCases[i][0], testCases[i][1]) + '\n');
}