/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    let returnArray = [];
    let temp = [];
    for(let i = 0; i < prices.length; i++)
    {
        
    }
};

testCases = [ [[8,4,6,2,3], [4,2,4,2,3]], [[1,2,3,4,5], [1,2,3,4,5]], [[10,1,1,6], [9,0,1,6]]];
for(const test of testCases)
{
    console.log('Input: ' + test[0] + '\nExpected output: ' + test[1] + '\nActual output: ' + finalPrices(test[0]) + '\n');
}