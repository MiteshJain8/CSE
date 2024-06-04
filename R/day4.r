# create a dataframe such as name age and usn , display it and order it based on the age, populate the dataframe with NA values and also deal with the missing values by using NA.argument() functions

names <- c("Kartik", "Joel", "Mitesh")
age <- c(22, 20, 21)
usn <- c("CS076", "CS075", "Cs085")
df <- data.frame( names, age, usn)
# print(df)
df
df[order(df$age), ]
df[order(df$name), ]

z <- 3
f <- function(x,y){
    # print("calc =",x^2+y/z)
    x^2+y/z
}
f(2,3)

x = as.raw(255)
# print(x)
x
class(x)
typeof(x)

y = 2
class(y)
typeof(y)
is.numeric(y)
is.double(y)

as.character(FALSE)
as.numeric(FALSE)

arr <- c(3,5,6,3,6,8)
sort(arr, decreasing = TRUE)
class(arr)
typeof(arr)
order(arr, decreasing = FALSE)
order(arr, decreasing = TRUE)
order(-arr)

z <- "mit"
z
class(z)
typeof(z)

w <- TRUE
w
class(w)
typeof(w)