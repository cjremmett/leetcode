/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function(words)
{
    let wordSet = new Set(words);
    let resultSet = new Set();

    for(let w of wordSet.values())
    {
        for(let i = 1; i < w.length; i++)
        {
            for(let j = 0; j < w.length + 1 - i; j++)
            {
                if(wordSet.has(w.substring(j, j+i)))
                {
                    resultSet.add(w.substring(j, j+i));
                }
            }
        }
    }

    return Array.from(resultSet);
    
};

let testCases = [ [ ["mass","as","hero","superhero"], ["as","hero"]], [["leetcode","et","code"], ["et","code"]]]

for(const testCase of testCases)
{
    console.log('Input: ' + testCase[0] + '\nExpected output: ' + testCase[1] + '\nActual output: ' + stringMatching(testCase[0]) + '\n');
}