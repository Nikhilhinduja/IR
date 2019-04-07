import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['This is the first document','This document is the second document','And this is the third one.',
        'Is this the first document?']
vectorizer=CountVectorizer()
X=vectorizer.fit_transform(corpus)
print("Fit transfer is")
print(X.toarray())
df=pd.DataFrame(X.toarray(),
                columns=vectorizer.get_feature_names())
print("the genearated data frame is")
print(df)
alldata=df[(df['this']==1) & (df['first']==1)]
print("Indices where both 'this' and 'first' terms are present are",alldata.index.tolist())
ordata=df[(df['this']==1) | (df['first']==1)]
print("Indices where either 'this' or 'first' terms are present are",ordata.index.tolist())
notdata=df[(df['and']!=1)]
print("Indices where AND term is not present", notdata.index.tolist())




#>>> a = 9
#>>> b = 6
#>>> print("Bitwise OR a|b", a|b)
#Bitwise OR a|b 15
#>>> print("Bitwise AND a&b",a & b)
#Bitwise AND a&b 0
#>>> print(a!=b)
#True

