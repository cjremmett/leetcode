/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    let return_string = '';
    for(let i = 0; i < s.length; i++)
    {
        let charCode = s.charCodeAt(i);
        let offset = 0;
        for(const shift of shifts)
        {
            if(i >= shift[0] && i <= shift[1])
            {
                if(shift[2] === 0)
                {
                    offset--;
                }
                else
                {
                    offset++;
                }
            }
        }
        offset = offset % 26;

        charCode = charCode + offset;
        if(charCode < 97)
        {
            charCode = 123 - (97 - charCode);
        }
        else if (charCode > 122)
        {
            charCode = 96 + (charCode - 122);
        }

        return_string = return_string + String.fromCharCode(charCode);
    }

    return return_string;
};

let testCases = [ ["abc", [[0,1,0],[1,2,1],[0,2,1]], 'ace'], ["dztz", [[0,0,0],[1,1,1]], 'catz']];
for(const testCase of testCases)
{
    console.log('Input: ' + testCase[0] + ' ' + testCase[1] + '\nExpected output: ' + testCase[2] + '\nActual output: ' + shiftingLetters(testCase[0], testCase[1]) + '\n');
}