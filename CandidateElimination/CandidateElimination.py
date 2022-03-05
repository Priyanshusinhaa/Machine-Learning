dataset = [
    ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
    ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
    ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'],
    ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes'],
]

class CandidateElimination:
    def __init__(self, hypothesis, hypothesis_ds):
        #hypothesis_ds is a Hypothesis dataset
        self.h0 = hypothesis
        self.h_ds = hypothesis_ds

    def find(self):
        generic_2d = []
        for n in range(len(self.h_ds)):
            if self.h_ds[n][-1] == 'yes': # for yes examples
                for m in range((len(self.h_ds[n])-1)):
                    if self.h0[m] != self.h_ds[n][m]:
                        self.h0[m] = '?'
            else: # for 'no' examples
                for m in range(len(self.h_ds[n])-1):
                    if self.h0[m] != self.h_ds[n][m]:
                        generic = []
                        generic.extend('?'*(len(self.h_ds[0])-1))
                        generic[m] = self.h0[m]
                        generic_2d.append(generic)
                
        #removing the contradiction
        generic_2dcpy = generic_2d[::]
        g, h = [], self.h0[:-1]
        g.extend('?'*(len(generic_2d[0])))
        for i in range(len(generic_2d)):
            for j in range(len(generic_2d[i])):
                if h[j] == '?':
                    if generic_2d[i][j] != '?':
                        generic_2dcpy.pop(i)

        #removing useless list from list
        gen = generic_2dcpy[::]
        for i in range(len(generic_2dcpy)):
            if gen[i] == g:
                gen.pop(i)

        return self.h0[:-1], gen


specific, generic = CandidateElimination(dataset[0], dataset).find()
print(specific, generic)