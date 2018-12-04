#Question 1
student <- list("Sam",1,F,c(89,75,91,78,85))

avrg <- mean(student[[4]])
avrg

rolln_mark_list <- list(student[[2]],student[[4]])

student[[4]][5]=100

subject_list <- c("maths","physics","biology","english","chemistry")
list(student,subject_list)


#Question 2
A <- matrix(8:11,nrow=2)
B <- 2*(A)

#Question 3
M <- matrix(c(1,1,3,5,2,6,-2,-1,-3),nrow=3,byrow=T)
M%*%M%*%M

#Question 4
N <- matrix(c(10,-10,10),nrow=15,ncol=3,byrow=T)
N_T <- t(N)
transpose <- N_T%*%N


#Question 5
mat_5_a <- matrix(c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),nrow=3)
#mat_5_b <- matrix((mat_5_a))
dimnames(mat_5_a) = list(c("Alice","Bill","Sara"),c("p1","p2","p3","p4","p5"))

mat_5_c1 <- mean(mat_5_a[,1])
mat_5_c2 <- mean(mat_5_a[,2])
mat_5_c3 <- mean(mat_5_a[,3])
mat_5_c4 <- mean(mat_5_a[,4])
mat_5_c5 <- mean(mat_5_a[,5])

#Question 6
category <- factor(c("computers","speakers","printers","headphones"))
class(category)
