
students_skill = [['Writing','Reading','Painting','Programming','Googling', 'yes'], 
                   ['Writing','Reading','Humoristic','Programming', 'Googling', 'yes'],
                   ['Writing','Reading','Humoristic','Analytical Skill', 'googling', 'no'],
                   ['Writing','Reading','Optimistic','Programming', 'Yahooing', 'yes'],
                   ['Writing','Reading','Boxing','Reasoning','Binging', 'yes']]

dataset = [
    ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
    ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
    ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'],
    ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes'],
]
class FindS:
    def __init__(self, hypothesis_ds):
        #hypothesis_ds is a Hypothesis dataset
        self.h0 = hypothesis_ds[0]
        self.h_ds = hypothesis_ds

    def mostSpecific(self): #finding most specific
        for n in range(len(self.h_ds)):
            if self.h_ds[n][-1] == 'yes': #for yes values
                for m in range(len(self.h_ds[n])):
                    if self.h0[m] != self.h_ds[n][m]:
                        self.h0[m] = '?'
        return self.h0[:-1] 

specific = FindS(dataset).mostSpecific()
print(specific)






