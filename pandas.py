#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd


# In[10]:


# 딕셔너리로 Series 정의
dict_data = {'a':1, 'b':2, 'c':3}
series_data = pd.Series(dict_data)
series_data


# In[11]:


# Series 값 확인하기
series_data.values


# In[12]:


# Series 자료형 확인하기
series_data.dtypes


# In[15]:


# 인덱스 교체
series_data = pd.Series([1, 2, 3], index = ['d', 'e', 'f'])
series_data


# In[16]:


# Sereis index만 확인하기
series_data.index


# In[18]:


#리스트로 Series 정의
list_data = ['2021-03-29', 3.14, 'ABC', 100, True]
series_data = pd.Series(list_data)
series_data


# In[20]:


# 튜플로 만들기
tuple_data = ('지영', '1990-01-08', '여', True)
series_data = pd.Series(tuple_data, index = ['이름', '생년월일', '성별', '학생여부'])
series_data


# In[21]:


series_data[['생년월일', '성별']]


# In[28]:


series_data[[0,3]]


# In[27]:


series_data[1:2]


# In[26]:


series_data['생년월일':'성별']


# In[31]:


# 데이터프레임 = 시리즈를 여러개 합친 자료형 
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
df


# In[32]:


# 리스트로 데이터프레임 만들기 -- 하나의 리스트가 하나의 행이 된다.
df = pd.DataFrame([[14, '남', '청량중'], [17, '여', '경희여중']],
                 index = ['준서', '예은'],
                 columns = ['나이', '성별', '학교'])
df


# In[33]:


df.index


# In[34]:


df.columns


# In[35]:


df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']


# In[37]:


df


# In[39]:


# 열 이름 변경
df.rename(columns={'연령':'나이', '남녀':'성별', '소속':'학교'}, inplace=True)
df


# In[41]:


# 행 이름 변경
df.rename(index={'학생1':'준서', '학생2':'예은'}, inplace=True)
df


# In[42]:


exam_data = {'수학':[90,80,70], '영어':[98,89,95],
            '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data, index=['학생1', '학생2', '학생3'])
df


# In[43]:


# 행 삭제 : drop()
# 행을 삭제하려면 axis=0  -- 디폴트 값이라 생략 가능
# 열을 삭제하려면 axis=1  -- 꼭 지정

df2 = df.copy()
df2.drop('학생2', inplace=True)
df2


# In[44]:


# 열 삭제 -- 2개 이상을 삭제하려면 대괄호로 표시하기
df3 = df.copy()
df3.drop(['영어','음악'], axis=1, inplace=True)
df3


# In[50]:


# 행 선택
# 데이터프레인 인덱싱 : lob, iloc
# loc : 이름으로 인덱싱
# iloc : 숫자로 인덱싱

exam_data = {'수학':[90,95,100], '영어':[98,99,90], '음악':[100,90,95], '체육':[90,92,100]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])

label1 = df.loc['서준']
position1 = df.iloc[0]


# In[53]:


df


# In[51]:


label1


# In[52]:


position1


# In[54]:


list(label1)


# In[55]:


tuple(label1)


# In[56]:


dict(label1)


# In[57]:


# 두 개 이상의 행 선택 
label2 = df.loc[['서준', '우현']]
label2


# In[62]:


label3 = df.loc['서준':'우현']
label3


# In[58]:


position2 = df.iloc[[0,1]]
position2


# In[63]:


position3 = df.iloc[0:1]
position3


# In[64]:


exam_data = {'이름':['서준', '우현', '인아']
            , '수학':[90, 80, 70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
df


# In[67]:


# 열 선택
# df.열이름 또는 df['열이름']
math = df['수학']
math


# In[68]:


english = df.영어
english


# In[69]:


# 두 개 이상의 열 선택하기
music_pe = df[['음악', '체육']]
music_pe


# In[70]:


math_df = df[['수학']]
math_df


# In[76]:


# 범위 슬라이싱
exam_data = {'이름':['서준', '우현', '인아', '현이', '철수']
            , '수학':[90,80,70,100,99], '영어':[100,98,97,96,98]
            , '음악':[99,100,72,90,100], '체육':[95,97,98,100,90]}
df = pd.DataFrame(exam_data)

# 모든 행을 2행 간격으로 선택
df.iloc[::2]


# In[74]:


# 0행부터 2행까지 2행 간격으로 선택
df.iloc[0:3:2]


# In[75]:


# 모든 행을 -1행 간격으로 선택 = 역순으로 정렬
df.iloc[::-1]


# In[83]:


# 특정 열을 인덱스로 부여하기
exam_data = {'이름':['서준','우현','인아']
             ,'수학':[90,80,70], '영어':[98,89,95],
            '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
df


# In[84]:


df.loc['서준', '음악']


# In[85]:


df.iloc[0,2]


# In[86]:


df.loc['서준', ['음악', '체육']]


# In[88]:


df.loc['서준', '음악':'체육']


# In[89]:


df.iloc[0,[2,3]]


# In[90]:


df.iloc[0,2:4]


# In[91]:


df.loc[['서준', '우현'],['음악','체육']]


# In[95]:


df.loc['서준':'우현','음악':'체육']


# In[96]:


df.iloc[[0,1],[2,3]]


# In[97]:


df.iloc[0:2,2:4]


# In[99]:


# 열 추가
exam_data = {'이름':['서준','우현','인아']
             ,'수학':[90,80,70], '영어':[98,89,95],
            '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
df['국어'] = 80
df


# In[102]:


# 행 추가
df.loc[3] = 10
df.loc[4] = ['현이',100,100,100,100,100]
df


# In[105]:


# 원소 값 변경하기
# 이름을 인덱스로 지정
exam_data = {'이름':['서준','우현','인아']
             ,'수학':[90,80,70], '영어':[98,89,95],
            '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
df


# In[106]:


# 서준의 체육 값 변경1
df.iloc[0][3] = 80
df


# In[107]:


# 서준의 체육 값 변경2
df.iloc[0,3]=75
df


# In[108]:


# 서준의 체육 값 변경3
df.loc['서준']['체육'] = 99
df


# In[110]:


# 서준의 체육 값 변경4
df.loc['서준','체육'] = 100
df


# In[111]:


exam_data = {'이름':['서준','우현','인아']
            , '수학':[90,80,70], '영어':[100,99,98], '음악':[87,88,89], '체육':[100,95,97]}
df = pd.DataFrame(exam_data)
df


# In[112]:


# 행과 열 바꾸기
df = df.transpose()
df


# In[113]:


df = df.T
df

