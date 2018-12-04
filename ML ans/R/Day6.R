#Question 1
age <- c(2,3,5,7,8)
weight <- c(14,20,32,42,44)
# a
regr <- lm(weight~age)
# b
k <- data.frame(age=6)
weight_6_age <- predict(regr,k)
# c
plot(age,weight)
abline(regr)

#Question 2
cust <- c(8,7,6,4,2,1)
dist <- c(15,19,25,23,34,40)
# a
cor(cust,dist)
# b
regr <- lm(cust~dist)
k <- data.frame(dist=2)
cust_2 <- predict(regr,k)
#c
regr <- lm(dist~cust)
k <- data.frame(cust=5)
dist_5 <- predict(regr,k)

#Question 3
mat <- c(6,4,8,5,3.5)
chem <- c(6.5,4.5,7,5,4)
relation <- lm(chem~mat)
k <- data.frame(mat=7.5)
chem_7.5 <- predict(relation,k)

#Question 4
h8 <- c(186,189,190,192,193,193,198,201,203,205)
w8 <- c(85,85,86,90,87,91,93,103,100,101)
#a
relation <- lm(w8~h8)
plot(h8,w8)
abline(relation)
#b
cor(h8,w8)
#c
k <- data.frame(h8=208)
w8_208 <- predict(relation,k)

#Question 6
sleep <- c(6,7,8,9,10)
tv <- c(4,3,3,2,1)
#a
cor(sleep,tv)
#b
relation <- lm(tv~sleep)
#c
k <- data.frame(sleep=8)
tv_8 <- predict(relation,k)


#Question 7
score <- c(25,42,33,54,29,36)
sales_dollar <- c(42,72,50,90,45,48)

cor(sales_dollar,score)

relation <- lm(sales_dollar~score)
k <- data.frame(score=47)
sales_47 <- predict(relation,k)








