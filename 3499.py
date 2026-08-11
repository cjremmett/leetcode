class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Construct segment list
        segments: list[tuple[int, int]] = []
        last_char_seen: int | None = None
        current_segment_range: list[int] | None = None
        for i in range(0, len(s)):
            if s[i] == last_char_seen:
                current_segment_range[1] += 1
                continue
            else:
                last_char_seen = s[i]
                if current_segment_range:
                    segments.append(current_segment_range)

                current_segment_range = [i, i + 1]

        if current_segment_range:
            segments.append(current_segment_range)

        # Get count of 1s
        count_ones: int = 0
        for i in range(0, len(s)):
            if s[i] == '1':
                count_ones += 1

        # Find largest two 0 zero segments separated by a single 1 segment between them
        largest_sum_seen: int = 0
        current_segment_index: int = 0
        if s[0] == '1':
            current_segment_index = 1

        print(f'Starting with index {current_segment_index}')

        for i in range(current_segment_index, len(segments), 2):
            if len(segments) > i + 2:
                current_sum: int = (segments[i][1] - segments[i][0]) + (segments[i+2][1] - segments[i+2][0])
                if current_sum > largest_sum_seen:
                    largest_sum_seen = current_sum
            else:
                current_sum: int = (segments[i][1] - segments[i][0])
                if current_sum > largest_sum_seen:
                    largest_sum_seen = current_sum

            print(f'Checked index {i}: current sum: {current_sum}')


        if len(segments) <= 2 or (len(segments) == 3 and s[0] == '1'):
            return count_ones
        return count_ones + largest_sum_seen 


if __name__ == '__main__':
    test_cases = [("01", 1), ("0100", 4), ("1000100", 7), ("01010", 4)]
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected output: {case[1]}\nActual output: {Solution().maxActiveSectionsAfterTrade(case[0])}\n')