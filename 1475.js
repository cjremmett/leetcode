/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    let returnArray = [...prices];
    let stack = [];
    for(let i = 0; i < prices.length; i++)
    {
        while(stack.length > 0 && prices[stack[stack.length-1]] >= prices[i])
        {
            let targetIndex = stack.pop();
            returnArray[targetIndex] = returnArray[targetIndex] - prices[i];
        }

        stack.push(i);
    }

    return returnArray;
};

testCases = [ [[8,4,6,2,3], [4,2,4,2,3]], [[1,2,3,4,5], [1,2,3,4,5]], [[10,1,1,6], [9,0,1,6]]];
for(const test of testCases)
{
    console.log('Input: ' + test[0] + '\nExpected output: ' + test[1] + '\nActual output: ' + finalPrices(test[0]) + '\n');
}