#Question 1
sname <- c("Alex","Lilly","Mark")
age <- c(25,31,23)
height <- c(177,163,190)
weight <- c(57,69,83)
sex <- c("F","F","M")
S <- data.frame(age,height,weight,sex)
rownames(S) <- sname

#Question 2
working <- c("Yes","No","No")
S_f <- cbind(S,working)

#Question 2_a
a <- S_f[,1]
class(a)
h <- S_f[,2]
class(h)
w <- S_f[,3]
class(w)
s <- S_f[,4]
class(sex)
wk <- S_f[,5]
class(wk)

#Question 2_b
mean(h)

#Question 2_c
hm <- h/100
BMI_df <- w/(hm*hm)
S_final <- cbind(S_f,BMI_df)

#Question 2_d
healthy <- c("True","False","True")
cbind(S_final,healthy)


#Question 3
r1 <- read.table(file.choose())

#Question 4
r2 <- read.csv(file.choose())

#Question 5
row_name <- c('r1','r2')
col_name <- c('c1','c2','c3')
matrix_name <- c('m1','m2','m3')

array_needed <- array(data=c(1:20), dim=c(2,3,3),dimnames=c(row_name,col_name,matrix_name))
array_needed

#Question 6_a
mpg <- mtcars$mpg
cyl <- mtcars$cyl
hp <- mtcars$hp
mtcars_working <- data.frame(rownames(mtcars),mpg,cyl,hp)

#Question 6_b
first_5 <- head(mtcars,5)
last_5 <- tail(mtcars,5)
mtcars_final <- rbind(first_5,last_5)

#Question 7_a
add <- function(a,b=1)
{
  x <- a+b
  print(x)
}
add(1,)

