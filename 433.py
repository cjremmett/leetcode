from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        self.bank_set = set(bank)
        self.adjacency_list = {gene:set() for gene in bank}
        self.adjacency_list[startGene] = set()
        self.gene_chars = ['A', 'C', 'G', 'T']
        for gene in bank:
            for i in range(0, 8):
                for char in self.gene_chars:
                    temp_gene = gene[0:i] + char + gene[i + 1:]
                    if temp_gene in self.bank_set:


if __name__ == '__main__':
    test_cases = (["AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1], ["AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2])
    for case in test_cases:
        print('Start gene: ' + case[0] + ' End gene: ' + case[1] + ' Bank: ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().minMutation(case[0], case[1], case[2])) + '\n')