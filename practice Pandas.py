#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np


# In[2]:


titanic_df = pd.read_csv('titanic_train.csv')
print('titanic 변수 type:', type(titanic_df))


# In[4]:


titanic_df.head()


# **Data Frame 생성**

# In[10]:


dic1 = {
    "Name": ['Jiyeong', 'Daehan', 'Jiyeon', 'SangCheol'],
    "Year": [1990, 1985, 1960, 1960],
    "Gender": ['Female', 'Male', 'Female', 'Male'] 
}

# 딕셔너리를 DataFrame으로 변환
data_df = pd.DataFrame(dic1)
print(data_df)
print("#"*30)

# 새로운 컬럼명을 추가
data_df = pd.DataFrame(dic1, columns=["Name", "Year", "Gender", "Age"])
print(data_df)
print("#"*30)

# 인덱스를 새로운 값으로 할당
data_df = pd.DataFrame(dic1, index=['one', 'two', 'three', 'four'])
print(data_df)
print("#"*30)


# **DataFrame의 컬럼명과 인덱스**

# In[11]:


print("columns:", titanic_df.columns)
print("index:", titanic_df.index)
print("index value:", titanic_df.index.values)


# **DataFrame에서 Series 추출 및 DataFrame 필터링 추출**

# In[18]:


# DataFrame 객체에서 [] 연산자 내에 한 개의 컬럼만 입력하면 Series 객체를 반환
series = titanic_df['Name']
print(series.head(3))
print("## type:", type(series))

# DataFrame 객체에서 [] 연산자 내에 여러 개의 컬럼을 리스트로 입력하면, 그 컬럼들로 구성된 DataFrame을 반환
filtered_df = titanic_df[['Name', 'Age']]
print(filtered_df.head(3))
print("## type:", type(filtered_df))

# DataFrame 객체에서 [] 연산자 내에 한 개의 ㅋ러럼을 리스트로 입력하면, 한 개의 컬럼으로 구성된 DataFrame을 반환
one_col_df = titanic_df[['Name']]
print(one_col_df.head(3))
print("## type:", type(one_col_df))


# **shape : DataFrame의 행과 열의 크기**

# In[19]:


print('DataFrame의 크기:', titanic_df.shape)


# **info() : DataFrame 내의 컬럼명, 데이터 타입, Null 건수, 데이터 건수 정보를 제공**

# In[20]:


titanic_df.info()


# **describe() : 데이터값들의 평균, 표준편차, 4분위분포도를 제공한다. (숫자 컬럼들에 대해서)**

# In[21]:


titanic_df.describe()


# **value_counts() : 동일한 데이터 값이 몇 건이 있는지 정보를 제공한다. Series 객체에서만 호출 될 수 있다.**

# In[25]:


value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)


# In[27]:


titanic_pclass = titanic_df['Pclass']
print(type(titanic_pclass))


# In[28]:


titanic_pclass.head()


# **sort_values() by=정렬컬럼, ascending=True 또는 False로 오름차순/내림차순 정렬**

# In[32]:


titanic_df.sort_values(by='Pclass', ascending=True).head()


# In[34]:


titanic_df.sort_values(by='Pclass', ascending=False).head()


# In[36]:


titanic_df[['Name', 'Age']].sort_values(by='Age').head()


# In[38]:


titanic_df[['Name', 'Age', 'Pclass']].sort_values(by=['Pclass', 'Age']).head()


# **리스트, ndarray에서 DataFrame 변환**

# In[45]:


col_name1 = ['col1']
list1 = [1,2,3]
array1 = np.array(list1)

print('array1 shape:', array1.shape)
df_list1 = pd.DataFrame(list1, columns=col_name1)
print('1차원 리스트로 만든 DataFrame:\n', df_list1)
df_array1 = pd.DataFrame(array1, columns=col_name1)
print('1차원 ndarray로 만든 DataFrame:\n', df_array1)


# In[47]:


# 딕셔너리에서 DataFrame 변환

dict = {'col1':[1,11], 'col2':[2,22], 'col3':[3,33]}
df_dict = pd.DataFrame(dict)
print(df_dict)


# In[49]:


# DataFrame을 ndarray로 변환

array3 = df_dict.values
print('df_dict.values 타입:', type(array3), 'df_dict.values shape:', array3.shape)
print(array3)


# In[50]:


# DataFrame을 리스트로 변환

list3 = df_dict.values.tolist()
print('df_dict.values.tolist() 타입:', type(list3))
print(list3)


# In[52]:


# DataFrame을 딕셔너리로 변환

dict3 = df_dict.to_dict('list')
print('df_dict.to_dict의 타입:', type(dict3))
print(dict3)


# **DataFrame의 컬럼 데이터 셋** 

# In[55]:


titanic_df['Age_0']=0
titanic_df.head(3)


# **DataFrame 데이터 삭제**

# In[57]:


# axis에 따른 삭제
# axis=1 : 열 (axis=0 : 행)
titanic_drop_df = titanic_df.drop('Age_0', axis=1)
titanic_drop_df.head(3)


# In[59]:


titanic_df.head(3)


# In[64]:


drop_result = titanic_df.drop(['Age_0'], axis=1, inplace=True)
print('inplace=True 로 drop 후 반환된 값:', drop_result)


# **Index 객체**

# In[69]:


# 원본 파일 재 로딩
titanic_df = pd.read_csv('titanic_train.csv')
# Index 객체 추출
indexes = titanic_df.index
print(indexes)
# Index 객체를 실제 값 array로 변환
print('index 객체 array 값:\n', indexes.values)


# In[71]:


# reset Index

titanic_reset_df = titanic_df.reset_index(inplace=False)
titanic_reset_df.head()

