/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function(words)
{
    return [];
};

let testCases = [ [ ["mass","as","hero","superhero"], ["as","hero"]], [["leetcode","et","code"], ["et","code"]]]

for(const testCase of testCases)
{
    console.log('Input: ' + testCase[0] + '\nExpected output: ' + testCase[1] + '\nActual output: ' + stringMatching(testCase[0]) + '\n');
}