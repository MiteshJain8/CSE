# Syntax: hist(vector,main,xlab,ylab,xlim,ylim,breaks)
month<-c("Jan", "Feb", "Mar", "Apr")
rev<-c(12, 15, 2, 7, 9, 2, 5, 1, 23, 26, 22, 34, 31, 38, 35)
hist(rev,main="REV CHART", xlab="Months", ylab="Revenue", breaks = 8)

# library(airquality)
# data(airquality)
# hist(airquality$Temp,main="temerature chart",xlab="temp(F)",xlim=c(50,120),col="yellow",freq=TRUE)