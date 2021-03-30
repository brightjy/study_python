#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
# numpy 배열 구조나 랜덤 값 생성
import numpy as np
# matplotlib 그래프 그리기
import matplotlib.pyplot as plt


# In[4]:


dates = pd.date_range('20210401', periods=6)
dates


# In[8]:


df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df


# In[9]:


df.head(2)


# In[10]:


df.tail(3)


# In[11]:


df.describe()


# In[12]:


df.T


# In[13]:


df.sort_index(axis=1, ascending=False)


# In[14]:


df.sort_index(axis=0, ascending=False)


# In[15]:


df['A']


# In[16]:


type(df['A'])


# In[17]:


df.loc['2021-04-01']


# In[18]:


df.loc[dates[0]]


# In[19]:


df.loc['20210401']


# In[20]:


df.loc[dates[0], 'A']


# In[21]:


df.at[dates[0], 'A']


# In[22]:


df.iloc[3]


# In[23]:


df[df.A > 0]


# In[24]:


df[df > 0]


# In[25]:


df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df2


# In[28]:


df2['E'].isin(['one', 'four'])


# In[27]:


df2[df2['E'].isin(['one', 'four'])]


# In[30]:


df.loc[:,'D'] = np.array([5]*len(df))
df


# In[32]:


s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20210401', periods=6))
df['F'] = s1
df


# In[36]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
df1


# In[38]:


df1.dropna(how='any')


# In[39]:


df1.fillna(value=5)


# In[40]:


pd.isna(df1)


# In[41]:


# 컬럼 별 평균 (결측치 제외 후 연산)
df.mean()


# In[42]:


# 인덱스 별 평균 
df.mean(1)


# In[43]:


df.apply(np.cumsum)


# In[47]:


# 히스토그램
s = pd.Series(np.random.randint(0,7, size=10))
s.value_counts()


# In[52]:


# 문자열 관련 메소드
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()


# In[53]:


s.str.upper()


# In[55]:


# 합치기 - concat : 같은 형태의 자료들을 이어 하나로.
df = pd.DataFrame(np.random.randn(10,4))
df


# In[57]:


# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
pieces


# In[58]:


pd.concat(pieces)


# In[65]:


# 합치기 - merge : 다른 형태의 자료들을 한 컬럼을 기준으로 합침 ; join
left = pd.DataFrame({'key':['foo', 'bar'], 'lval':[1,2]})
left


# In[66]:


right = pd.DataFrame({'key':['foo', 'bar'], 'rval':[4,5]})
right


# In[67]:


merged = pd.merge(left, right, on='key')
merged


# In[68]:


# merge 할 때 key에 중복값이 있는 경우
left = pd.DataFrame({'key':['foo', 'foo'], 'lval':[1,2]})
right = pd.DataFrame({'key':['foo','foo'], 'rval':[4,5]})
merged = pd.merge(left, right, on='key')
merged


# In[69]:


# 합치기 - append : 데이터프레임 맨 뒤에 행을 추가
df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
df


# In[70]:


s = df.iloc[3]
s


# In[71]:


df.append(s, ignore_index=True)


# In[73]:


# Grouping

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})
df


# In[74]:


df.groupby('A').sum()


# In[75]:


df.groupby(['A','B']).sum()


# In[76]:


df.groupby(['B','A']).sum()


# In[ ]:


# stack : 데이터프레임의 컬럼들을 인덱스 레벨로 만든다.


# In[83]:


tuples = list(zip(*[
    ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(8,2), index=index, columns=['A', 'B'])

df2 = df[:4]


# In[85]:


stacked = df2.stack()
stacked


# In[86]:


# unstack() : stack() 되돌리기

stacked.unstack()


# In[87]:


# 해체 수준 지정해서 해체하기 : first를 컬럼으로

stacked.unstack(0)


# In[88]:


# 해체 수준 지정해서 해체하기 : second 를 컬럼으로

stacked.unstack(1)


# In[ ]:


# pivot tables


# In[90]:


df = pd.DataFrame({
    'A': ['one', 'one', 'two', 'three']*3,
    'B': ['A', 'B', 'C']*4,
    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar']*2,
    'D': np.random.randn(12),
    'E': np.random.randn(12)
})
df


# In[91]:


pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])


# In[96]:


# 시계열 데이터 다루기 Time Series

rng = pd.date_range('1/1/2021', periods=100, freq='S')

ts = pd.Series(np.random.randint(0,500,len(rng)),index=rng)

ts.resample('5Min').sum()


# In[100]:


# 타임존 표현

rng = pd.date_range('3/30/2021 00:00', periods=5, freq='D')

ts = pd.Series(np.random.randn(len(rng)), rng)

ts


# In[102]:


ts_utc = ts.tz_localize('UTC')

ts_utc


# In[103]:


# 타임존 변경

ts_utc.tz_convert('US/Eastern')


# In[106]:


# 시간 표현법으로 정리하기

rng = pd.date_range('1/1/2021', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts


# In[108]:


ps = ts.to_period()
ps


# In[109]:


ps.to_timestamp()


# In[110]:


prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
prng


# In[112]:


ts = pd.Series(np.random.randn(len(prng)), prng)
ts


# In[115]:


ts.index = (prng.asfreq('M', 'e')+1).asfreq('H', 's') + 9
ts.index


# In[118]:


ts.head(10)


# In[120]:


# 범주형 데이터 다루기

df = pd.DataFrame({
    "id": [1,2,3,4,5,6],
    "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']
})

df


# In[122]:


df["grade"] = df["raw_grade"].astype("category")

df["grade"]


# In[124]:


df["grade"].cat.categories = ["very good", "good", "not bad"]

df["grade"]


# In[126]:


df["grade"] = df["grade"].cat.set_categories(["bad", "not bad", "so so", 
                                              "good", "very good"])

df["grade"]


# In[127]:


df.sort_values(by="grade")


# In[128]:


df.groupby("grade").size()


# In[133]:


# 그래프로 표현하기

ts = pd.Series(np.random.randn(1000), 
               index=pd.date_range('1/1/2021', periods=1000))
ts = ts.cumsum()
ts.plot()


# In[134]:


df = pd.DataFrame(np.random.randn(1000,4),
                  index=ts.index,
                  columns=['A', 'B', 'C', 'D']  
                 )
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc='best')


# In[135]:


plt.figure();
df.iloc[5].plot(kind="bar");


# In[136]:


plt.figure();
df.iloc[5].plot.bar();


# In[137]:


df2 = pd.DataFrame(np.random.rand(10,4), columns=["a","b","c","d"])


# In[138]:


df2.plot.bar();


# In[139]:


df2.plot.bar(stacked=True);


# In[140]:


df2.plot.barh(stacked=True)


# In[142]:


# Histograms

df3 = pd.DataFrame(
    {
        "a": np.random.randn(1000) + 1,
        "b": np.random.randn(1000),
        "c": np.random.randn(1000) - 1
    },
    columns=["a","b","c"]
)

df3


# In[143]:


plt.figure();
df3.plot.hist(alpha=0.5);


# In[144]:


plt.figure();
df3.plot.hist(stacked=True, bins=20);


# In[145]:


plt.figure();
df3["a"].plot.hist(orientation="horizontal", cumulative=True)


# In[159]:


plt.figure();
df["A"].diff().hist(color="k", alpha=0.3, bins=500);


# In[147]:


plt.figure();
df.diff().hist(color="k", alpha=0.5, bins=50);


# In[160]:


data = pd.Series(np.random.randn(1000))
data


# In[163]:


data.hist(by=np.random.randint(0,4,1000), figsize=(6,4));


# In[164]:


# 데이터 입출력 - 데이터 프레임을 엑셀 파일로 저장하기
df.to_excel('foo.xlsx', sheet_name='sheet1')
pd.read_excel('foo.xlsx', 'sheet1', index_col=None, na_values=['NA'])

