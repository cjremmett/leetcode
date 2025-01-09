/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    for(const shift of shifts)
    {
        let start = s.substring(0, shift[0]);
        let end = s.substring(shift[1] + 1);
        let shifted = s.substring(shift[0], shift[1] + 1);
        let shifted_post = '';
        for(let i = 0; i < shifted.length; i++)
        {
            let cc = shifted.charCodeAt(i);
            if(shift[2] === 1)
            {
                cc++;
            }
            else
            {
                cc--;
            }
            
            if(cc === 96)
            {
                cc = 122;
            }
            else if(cc === 123)
            {
                cc = 97;
            }

            shifted_post = shifted_post + String.fromCharCode(cc);
        }
        s = start + shifted_post + end;
    }

    return s;
};

let testCases = [ ["abc", [[0,1,0],[1,2,1],[0,2,1]], 'ace'], ["dztz", [[0,0,0],[1,1,1]], 'catz']];
for(const testCase of testCases)
{
    console.log('Input: ' + testCase[0] + ' ' + testCase[1] + '\nExpected output: ' + testCase[2] + '\nActual output: ' + shiftingLetters(testCase[0], testCase[1]) + '\n');
}