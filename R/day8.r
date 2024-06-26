x <- c(3,6,7,7,NA,14,NA,22,24)
range(x,na.rm = TRUE)
IQR(iris$Sepal.Length,0.25)
IQR(iris$Sepal.Length,0.75)
IQR(iris$Sepal.Length)

library(moments)
skewness(x, na.rm = TRUE)

summary(iris, na.rm=FALSE)