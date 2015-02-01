__author__ = 'basnal'

class TimeKeeper:
    Hour = 0
    Min = 0
    Sec = 0
    TotalSec = 0
    TotalMinutes = 0

    def formatToTime(self, number):
        self.TotalSec = number
        self.TotalMinutes = number / 60
        self.Min, self.Sec = divmod(number, 60)
        self.Hour, self.Min = divmod(self.Min, 60)

    def printTime(self):
        print "%d:%02d:%02d" % (self.Hour, self.Min, self.Sec)