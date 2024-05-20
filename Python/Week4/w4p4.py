# Develop a python program to create a class called as TimeClass with attributes like seconds, minutes and hours. All the attributes must be of type integer. Write the constructor to initialize the attributes. Write methods to displayTime() to display the time in hh:mm:ss format, addTime(time) to add two times and display in hh:mm:ss format, subtractTime() to subtract two times and display in hh:mm:ss format and countSeconds() to display in total number of seconds in the given time

class Time:
    def __init__(self, seconds, minutes, hours):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def displayTime(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def addTime(self, time):
        sec = self.seconds + time.seconds
        min = self.minutes + time.minutes
        hr = self.hours + time.hours
        if sec >= 60:
            sec -= 60
            min += 1
        if min >= 60:
            min -= 60
            hr += 1
        return f"{hr}:{min}:{sec}"

    def subtractTime(self, time):
        count_self = self.hours*3600+self.minutes*60+self.seconds
        count_time = time.hours*3600+time.minutes*60+time.seconds
        if count_self < count_time:
            return "Time cannot be negative"
        sec = self.seconds - time.seconds
        min = self.minutes - time.minutes
        hr = self.hours - time.hours
        if sec < 0:
            sec += 60
            min -= 1
        if min < 0:
            min += 60
            hr -= 1
        return f"{hr}:{min}:{sec}"

    def countSeconds(self):
        count = self.hours*3600+self.minutes*60+self.seconds
        return abs(count)

t1 = Time(30, 20, 10)
t2 = Time(20, 30, 40)
print(f"t1 = {t1.displayTime()}")
print(f"t2 = {t2.displayTime()}")
print(f"t1-t2 = {t1.subtractTime(t2)}")
print(f"t2-t1 = {t2.subtractTime(t1)}")
print(f"t1+t2 = {t2.addTime(t1)}")
print(f"t1 in seconds: {t1.countSeconds()}")