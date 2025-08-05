class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result_string = ''
        da = [26]
        original = columnNumber
        columnNumber -= 26
        while columnNumber > 0:
            da.append(da[-1] * 26)
            columnNumber -= da[-1]
        da.pop()

        columnNumber = original
        while len(da) > 0:
            count = columnNumber // da[-1]
            cc = columnNumber // da[-1]
            if cc == 0:
                cc = 26
            if columnNumber % da[-1] == 0:
                count -= 1
                cc -= 1
            result_string = result_string + chr(64 + cc)
            columnNumber -= count * da[-1]
            da.pop()

        cc = columnNumber % 26
        if cc == 0:
            cc = 26
        result_string = result_string + chr(64 + cc)

        return result_string


if __name__ == '__main__':
    test_cases = ( (1, 'A'), (28, 'AB'), (701, 'ZY'), (52, 'AZ'))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected Output: {case[1]}\nActual Output: {Solution().convertToTitle(case[0])}\n')