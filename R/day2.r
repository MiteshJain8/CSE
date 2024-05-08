# Default parameter
addnum2 <- function(a=10, b=10,c){
    return(a+b)
}

# Function Defn
addnum <- function(a, b){
    return(a+b)
}
# Inline fn
sqofsumof2 = function(a, b) a^2+b^2+2*a*b

# Multiple I/p Multiple O/p

Rectangle = function(l = 0, b=0){
    area = l*b
    peri = 2*(l+b)

    result = list("Area"= area, "Peri"=peri )
    return(result)
}


print(sqofsumof2(2,1))

print(addnum2(1,3))
sum3 = addnum2(35,3.8)
sum2 = addnum2(a=29,3.8)
sum1 = addnum2(6)
sum0 = addnum2()

print(sum3)
print(sum2)
print(sum1)
print(sum0)

print(Rectangle(10,20))

rect = Rectangle(1,2)
print(rect["Area"])
print(rect["Peri"])
help(median)


# DATA STRUCTURES

# List
arr = c(1,2, "sgjds")
arr2 = c(1,2, 3)

print(arr)
print(arr2)