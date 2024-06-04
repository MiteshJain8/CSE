# Syntax: barplot(Vector, xlab, ylab, main, names.arg, col)

month<-c("Jan", "Feb", "Mar", "Apr")
rev<-c(423, 45, 56, 546)
barplot(rev, names.arg=month, xlab="Months", ylab="Revenue", col=terrain.colors(length(month)), main="REV CHART")

# barplot(airquality$Ozone,ylab="ozone levels",horiz=FALSE,col="red")