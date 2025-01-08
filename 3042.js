/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) 
{
    let count = 0;
    for(let i = 0; i < words.length; i++)
    {
        for(let j = i + 1; j < words.length; j++)
        {
            let prefix = words[j].substring(0, words[i].length);
            let suffix = words[j].substring(words[j].length - words[i].length);
            if(prefix === words[i] && suffix === words[i])
            {
                count ++;
            }
        }
    }

    return count;
};

let testCases = [ [["a","aba","ababa","aa"], 4], [["pa","papa","ma","mama"], 2]];
for(const test of testCases)
{
    console.log('Input: ' + test[0] + '\nExpected output: ' + test[1] + '\nActual output: ' + countPrefixSuffixPairs(test[0]) + '\n');
}