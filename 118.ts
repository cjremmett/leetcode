function generate(numRows: number): number[][] {
    if(numRows < 1)
    {
        return [[]];
    }
    else if(numRows === 1)
    {
        return [[1]];
    }
    else if(numRows === 2)
    {
        return [[1], [1,1]];
    }

    let rows: Array<Array<number>> = [[1],[1,1]];
    for(let i = 3; i <= numRows; i++)
    {
        let newRow = [1];
        for(let j = 1; j <= i-2; j++)
        {
            newRow.push(rows[i-2][j-1] + rows[i-2][j]);
        }
        newRow.push(1);
        rows.push(newRow);
    }

    return rows;
};

let testCases: Array<Array<any>> = [ [5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]], [1, [[1]]] ];
for(const testcase of testCases)
{
    console.log(`Input: ${testcase[0]}
        Expected output: ${JSON.stringify(testcase[1])}
        Actual output: ${JSON.stringify(generate(testcase[0]))}
        `);
}