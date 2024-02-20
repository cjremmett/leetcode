from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        self.bank_set = set(bank)
        self.adjacency_list = {gene:set() for gene in bank}
        self.adjacency_list[startGene] = set()
        self.gene_chars = ['A', 'C', 'G', 'T']
        for gene in self.adjacency_list:
            for i in range(0, 8):
                for char in self.gene_chars:
                    temp_gene = gene[0:i] + char + gene[i + 1:]
                    if temp_gene in self.bank_set and temp_gene != gene:
                        self.adjacency_list[gene].add(temp_gene)

        self.prev_genes = set()
        self.prev_genes.add((startGene))
        self.most_recent_prev_genes = (startGene, )
        self.current_genes = set()
        self.iteration = 0
        while True:
            self.iteration += 1

            for gene in self.most_recent_prev_genes:
                for gene_adj in self.adjacency_list[gene]:
                    self.current_genes.add(gene_adj)

            if endGene in self.current_genes:
                return self.iteration
            elif tuple(self.current_genes) in self.prev_genes:
                return -1
            else:
                self.prev_genes.add(tuple(self.current_genes))
                self.most_recent_prev_genes = tuple(self.current_genes)
                self.current_genes = set()
                

if __name__ == '__main__':
    test_cases = (["AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1], ["AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2])
    for case in test_cases:
        print('Start gene: ' + case[0] + ' End gene: ' + case[1] + ' Bank: ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().minMutation(case[0], case[1], case[2])) + '\n')