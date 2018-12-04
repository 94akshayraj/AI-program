vec_1_a <- c(1:20,19:1)
vec_1_a
x <- c(4,6,3)

#Question 2
vec_2_a <- rep(x,10)
vec_2_b <- rep(x,10,len = 31)
vec_2_c <- rep(x,each = 10,times=3)

vec_2_c

#Question 3
R <- c(2.27, 1.98, 1.69, 1.88, 1.64, 2.14)
H <- c(8.28, 8.04, 9.06, 8.70, 7.58, 8.34)
vec_vol <- 1/3*(pi*(R*R)*H)
round_vec_vol <- round(vec_vol,2)
round_vec_vol
minimum <- min(round_vec_vol)
maximum <- max(round_vec_vol)

#Question 4

A <- c(sample(0:999, 250))
B <- A[which(A >900)]
C <- c(sort(B))

#Question 5

H8 <- c(1.80, 1.65, 1.60, 1.93)
W8 <- c(87, 58, 65, 100)
BMI <- W8/(H8*H8)
BMI_W8_25 <- W8[which(BMI>25)]
BMI_AVG <- sum(BMI)/4

#Question 6
marks <- c(sample(0:50,10,replace=TRUE))
p1 <- mean(marks)
p2 <- median(marks)
