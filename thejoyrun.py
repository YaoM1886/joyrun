import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data

dfRun = pd.DataFrame({
    'date':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'minute':[60,61, 63, 69, 13, 63, 59, 76, 24,14],
    'second':[21, 6, 46, 21, 40, 37, 16, 15, 2,10],
    'distant':[6.26, 7.34, 7.36, 7.80, 1.42, 6.31, 6.03, 8.7, 2.64,1.46],
    'verocity':[6.22, 7.21, 6.93,6.75, 6.33, 5.96, 6.11, 6.85, 6.59,6.18],
    'Kcal':[1135, 1332, 1334, 1414, 258, 1144, 1094, 1577, 478,264],
    'total_walknum':[7333,8048, 8297, 8826, 1676, 7803, 7224, 9874, 3071,1744],
    'walkspeed':[121, 131, 130, 127, 124, 122, 121, 129, 127,123]
})


dfRun['second'] = dfRun['second']/60.0
dfRun['minute'] += dfRun['second']
dfRun.drop('second', axis=1, inplace=True)
# dfRun['Kcal'] /= dfRun['distant']
# k=0
# for i in dfRun['date'].values:
#     dfRun.loc[k, 'date'] = datetime.datetime.strptime(i, '%m/%d')
#     k+=1

print(dfRun)
#
# dfRun.plot(x='date', y='Kcal')
# plt.ylabel('Kcal')
# plt.show()



def main():
    x=dfRun['date']
    y=dfRun['Kcal']

    fig, ax = plt.subplots()
    imscatter(x, y, zoom=0.22, ax=ax)
    ax.plot(x, y)
    plt.xlabel('day number')
    plt.ylabel('Kcal')
    plt.title('How many Kcal(=1K calories) did I burn when running?')
    plt.show()

def imscatter(x, y, ax=None, zoom=1):
    i = 1
    for x0, y0 in zip(x, y):
        image = get_sample_data('/Users/mac/Desktop/%d.png' %i)
        if ax is None:
            ax = plt.gca()
        try:
            image=plt.imread(image)
        except TypeError:
            pass
        im = OffsetImage(image, zoom=zoom)
        artists=[]
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
        artists.append(ax.add_artist(ab))
        i+=1
    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()
    return artists


main()


