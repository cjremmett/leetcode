function containsDuplicate(nums: number[]): boolean {
    let numSet = new Set<number>;
    for(const num of nums)
    {
        if(numSet.has(num))
        {
            return true;
        }
        else
        {
            numSet.add(num);
        }
    }
    return false;
};

let testCases217: Array<Array<any>> = [ [[1,2,3,1], true], [[1,2,3,4], false], [[1,1,1,3,3,4,3,2,4,2], true]];
for(const testCase of testCases217)
{
    console.log(`
        Input: ${testCase[0]}
        Expected output: ${testCase[1]}
        Actual output: ${containsDuplicate(testCase[0])}
    `)
}