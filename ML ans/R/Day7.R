#Question 1
#a
die <- sample (1:6,300,replace = T)
#b
rand_number <- sample(30:70,27)
#c
coin <- sample(c("H","T"),1000,replace = T)

#Question 2
#a
r <- rnorm(100,0,30)
x <- round(r,2)
k <- dnorm(x,0,30) 
plot(x,k)
#b
k1 <- pnorm(x,0,30)
plot(x,k1)
#c
k2 <- qnorm(0.2,0,30)
check <- dnorm(-25.24864,0,30)
check <- pnorm(-25,0,30)
#d
k3 <- qnorm(0.5,0,30)

#Question 3
#a
r <- rnorm(100,0,15)
x <- round(r,2)
k <- dnorm(x,0,15) 
plot(x,k)
#b
k1 <- pnorm(x,0,15)
plot(x,k1)
#c
k2 <- qnorm(0.2,0,15)
check <- dnorm(-25.24864,0,15)
check <- pnorm(-25,0,15)
#d
k3 <- qnorm(0.5,0,15)

#Question 4
hista <- rnorm(5000,20,5)
hist(hista)
 
#Question 5
#a
1-(pnorm(29,22,5)) 
#b
pnorm(17,22,5)
(pnorm(15,22,5))+(1-(pnorm(25,22,5)))
#Question 6
last <- dnorm(31,30,2)
last <- 1/(sqrt(2*pi)*2)*exp(-((31 - 30)^2/(2*2^2)))

