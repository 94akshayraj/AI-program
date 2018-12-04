#Question_1_a
dbinom(5,50,.8)
#Question_1_b
dbinom(5,50,.05)
#Question_1_c
pbinom(5,50,.8)
#Question_1_d
1-pbinom(25,50,.8)
#Question_1_e
pbinom(5,50,.05)


#Question_2a
dbinom(40,60,.65)
#Question_2b
1-pbinom(40,60,.65)

#Question_3_a
x<- seq(0,30,1)
y <- dbinom(x,30,.15)
plot(x, y)
#Question_3_b
y <- dbinom(x,30,.4)
plot(x, y)
#Question_3_c
y <- dbinom(x,30,.8)
plot(x, y)
#Question_4_a
result <- pbinom(20,60,.5)+pbinom(25,60,.5)+pbinom(30,60,.5)
#Question_4_b
pbinom(20,60,.5)
#Question_4_c
pbinom(30,60,.5)+pbinom(20,60,.5)

#Question_5
dpois(100,50)
dpois(100,3)
dpois(100,4)
dpois(100,5)
dpois(100,1)

#Question_6
ques6 <- rpois(2608,10097/2608)
hist(ques6)

#Question_7
ppois(5,7)
1-ppois(10,7)
(1-ppois(4,7))-(1-ppois(16,7))

#Question_8
punif(6,0,25)
6/25

