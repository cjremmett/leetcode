/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) 
{
    let wordMap = new Map();
    for(let j = 0; j < words.length; j++)
    {
        for(let i = 1; i < Math.floor(word.length / 2); i++)
        {
            if(words[j].substring(0, i).equals(words[j].substring(words[j].length - i)))
            wordMap.set(), j)
        }
    }
};

let testCases = [ [["a","aba","ababa","aa"], 4], [["pa","papa","ma","mama"], 2]];
for(const test of testCases)
{
    console.log('Input: ' + test[0] + '\nExpected output: ' + test[1] + '\nActual output: ' + countPrefixSuffixPairs(test[0]) + '\n');
}