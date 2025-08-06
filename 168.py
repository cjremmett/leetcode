class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result_string = ''
        while columnNumber > 0:
            columnNumber -= 1
            char_code = columnNumber % 26
            result_string = chr(65 + char_code) + result_string
            columnNumber = columnNumber // 26
        
        return result_string
        
if __name__ == '__main__':
    test_cases = ( (1, 'A'), (28, 'AB'), (701, 'ZY'), (52, 'AZ'))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected Output: {case[1]}\nActual Output: {Solution().convertToTitle(case[0])}\n')