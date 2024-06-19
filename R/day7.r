x <- c(3,6,7,7,NA,14,NA,22,24)
mean(x, na.rm=TRUE)

str(iris)

mean(iris$Sepal.Length)
median(iris$Sepal.Length)

apply(iris[ , c('Sepal.Width', 'Sepal.Length')], 2, mean)
apply(iris[ , c('Sepal.Width', 'Sepal.Length')], 2, median)

with(iris, sort(table(iris$Sepal.Length), decreasing = FALSE))

var(iris$Sepal.Length, na.rm = FALSE)