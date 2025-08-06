function convertToTitle(columnNumber: number): string {
    let returnString = '';
    while(columnNumber > 0)
    {
        columnNumber--;
        returnString = String.fromCharCode(65 + (columnNumber % 26)) + returnString;
        columnNumber = Math.floor(columnNumber / 26);
    }
    return returnString;
};

let testCases: Array<[number, string]> = [ [1, 'A'], [28, 'AB'], [701, 'ZY']]
for(const testCase of testCases)
{
    console.log(`Input: ${testCase[0]}
        Expected output: ${testCase[1]}
        Actual output: ${convertToTitle(testCase[0])}`);
}