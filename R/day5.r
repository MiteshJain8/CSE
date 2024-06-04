# barplot(VADeaths, beside=TRUE, ylim=c(0,90), legend=TRUE)

# dotchart(VADeaths, xlim = c(0,75))

# grpsizes<-c(33, 45, 56, 23)
# labels<-c("A", "B", "C", "D")
# pie(grpsizes, labels)

# barplot(airquality$Ozone,ylab="ozone levels",horiz=FALSE,col="red")

# hist(airquality$Temp, freq=FALSE, breaks = 20)

# boxplot(Sepal.Length ~ Species, data = iris, boxwex = 0.5, varwidth=TRUE, notch=TRUE)

x<-rnorm(100)
y<-rpois(100,30)
a<-sort(x)
b<-sort(y)
plot(a, b, type="l", main="normal vs poisson")