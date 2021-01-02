import Honey
from Essencials import getFloat, getAnswer
import Statistic

data = []

while True:
    sample = getFloat ('Enter sample: ')
    data.append(sample)
    answer = getAnswer ('Do you want to add another sample? (Y/N): ')
    if answer == 'y':
        pass
    else:
        break
    if len(data) == 10:
        break

data1 = []

for sample in data:
    inverted_sugar = Honey.InvertedSugarInHoney(0.545, sample, 10)
    data1.append(inverted_sugar)
    print(*data1, sep = ', ')

dixon = Statistic.dixonTest(data1, 0.9)
ttest = Statistic.Ttest(dixon, 50, 0.95)

