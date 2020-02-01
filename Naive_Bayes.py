class Naive_Bayes:

  def __init__(self, px_c):

    self.c = [0.36363636363636365, 2.8181818181818183, 2.272727272727273, 2.8181818181818183, 2.909090909090909, 2.272727272727273, 1.0909090909090908, 2.5454545454545454, 0.2727272727272727, 0.8181818181818182, 0.45454545454545453]
    #self.px_c = [[[self.count_tup(i,j,k)/(self.c[k]*self.n_tup) for k in range(self.n_classes)] for j in range(self.n_classes)] for i in range(self.n_attr)]
    self.px_c = px_c

  def predict(self, condition):

    p_y = 1
    for i in range(len(condition)):
      p_y = p_y*self.px_c[i][condition[i]][1]
    p_y = p_y*self.c[1]


    p_n = 1
    for i in range(len(condition)):
      p_n = p_n*self.px_c[i][condition[i]][0]
    p_n = p_n*self.c[0]


    if p_y > p_n:
      return 1, p_y
    
    return 0, -1



#data = [[0,0], [0,0], [0,1], [1,1], [1,1], [0,1], [1,0], [0,0], [1,1], [0,0], [1,1], [0,0], [0,1], [1,1]]
#labels = [0,      0,     1,    1,     1,     0,     1,     0,     1,     1,     1,     1,     1,      0]
"""
nb = []
for i in range(11):

  data = []
  labels = []
  for j in range(len(training1)):
    data.append(training1[j][0])
    labels.append(training1[j][1][i])

  nb.append(Naive_Bayes(data, labels))
"""





