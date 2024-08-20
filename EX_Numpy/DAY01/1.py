import pandas as pd
import numpy as np
# %precision 3
# pd.set_option(['precision',3])

df=pd.read_csv(r'C:\Users\kdp\Desktop\KDW\EX_Numpy\ch2_scores_em.csv', index_col='student number')
df.head()

scores=np.array(df['english'])[:10]
scores

scores_df=pd.DataFrame({'score':scores}, index= pd.Index(['A','B','C','D','E','F','G','H','I','J'], name= 'student'))

sum(scores)/len(scores)
np.mean(scores)
scores_df.mean

sorted_scores=np.sort(scores)
print(sorted_scores)

n=len(sorted_scores)

if n %2==0:
    m0=sorted_scores[n//2-1]
    m1=sorted_scores[n//2]
    median=(m0+m1)/2
else:
    median=sorted_scores[(n+1)//2-1]

print(median)

print(pd.Series([1,1,1,2,2,3]).mode())

mean=np.mean(scores)
deviation=scores-mean
print(deviation)

summary_df=scores_df.copy()
summary_df['deviation']=deviation
print(summary_df)

print(summary_df.mean())

print(np.mean(deviation**2))
print(np.var(scores))

summary_df['square of deviation']= np.square(deviation)
print(summary_df)

print(summary_df.mean())

print(np.sqrt(np.var(scores,ddof=0)))
print(np.std(scores,ddof=0))

print(np.max(scores)-np.min(scores))

scores_Q1=np.percentile(scores,25)
scores_Q3=np.percentile(scores,75)
scores_IQR=scores_Q3-scores_Q1
print(scores_IQR)

print(pd.Series(scores).describe())

z=(scores-np.mean(scores)) / np.std(scores)
print(z)

print(np.mean(z), np.std(z,ddof=0))

z=50+10*(scores-np.mean(scores)) / np.std(scores)
print(z)

scores_df['deviation value']=z
print(scores_df)

english_scores=np.array(df['english'])
print(pd.Series(english_scores).describe())

freq,_=np.histogram(english_scores,bins=10, range=(0,100))
print(freq)

freq_class=[f'{i}~{i+10}' for i in range(0,100,10)]

freq_dist_df=pd.DataFrame({'frequency':freq}, index=pd.Index(freq_class, name='class'))

print(freq_dist_df)

class_value=[(i+(i+10))//2 for i in range(0,100,10)]
print(class_value)

rel_freq=freq/freq.sum()
print(rel_freq)

cum_rel_freq=np.cumsum(rel_freq)
print(cum_rel_freq)

freq_dist_df['class value']=class_value
freq_dist_df['relative frequency']=rel_freq
freq_dist_df['cumulative relative frequency']=cum_rel_freq
freq_dist_df=freq_dist_df[['class value','frequency','relative frequency','cumulative relative frequency']]

print(freq_dist_df)


print(freq_dist_df.loc[freq_dist_df['frequency'].idxmax(),'class value'])

import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
freq,_,_=ax.hist(english_scores, bins=10, range=(0,100))
ax.set_xlabel('score')
ax.set_ylabel('person number')
ax.set_xticks(np.linspace(0,100,10+1))
ax.set_yticks(np.arange(0,freq.max()+1))
plt.show()

fig=plt.figure(figsize=(10,6))
ax1=fig.add_subplot(111)
ax2=ax1.twinx()

weights=np.ones_like(english_scores)/len(english_scores)
rel_freq,_,_=ax1.hist(english_scores,bins=25,range=(0,100), weights=weights)
cum_rel_freq=np.cumsum(rel_freq)
class_value=[(i+(i+4))//2 for i in range(0,100,4)]

ax2.plot(class_value,cum_rel_freq,ls='--',marker='o', color='gray')
ax2.grid(visible=False)

ax1.set_xlabel('score')
ax1.set_ylabel('relative frequency')
ax2.set_ylabel('cumulative relative frequency')
ax1.set_xticks(np.linspace(0,100,25+1))

plt.show()

fig=plt.figure(figsize=(5,6))
ax=fig.add_subplot(111)
ax.boxplot(english_scores,labels=['english'])

plt.show()

fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

x=range(0,100)
y=[v*v for v in x]
ax1.plot(x,y)
ax2.bar(x,y)

plt.show()
