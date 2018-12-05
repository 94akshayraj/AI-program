s1 = s(range(4),index=list("abcd"))
print s1.reindex(list("abcde")),"\n"
print s1.reindex(list("abcde"),method="ffill")
print s1.reindex(list("abcde"),method="bfill")

ad=np.arange(1,10).reshape(3,3)
df1=f(ad,columns=list("abc"),index=list("xyz"))
print df1,"\n"
print df1.reindex(list("yzx")),"\n"