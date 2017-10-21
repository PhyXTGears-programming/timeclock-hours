import math
import os
from datetime import datetime
from tkinter import filedialog

ioForm = "%H:%M:%S %d.%m.%Y"


def getSecs(fil):
    with open(fil, 'r') as userFile:
        totalTime = 0
        lastState = "n"
        lastTime = datetime.now()
        for currentLine in userFile:
            currentLine = currentLine.strip()
            if currentLine:
                time_str = currentLine[4:]
                state = currentLine[0]
                time = datetime.strptime(time_str, ioForm)
                if state == "i":
                    lastTime = time
                elif state == "o":
                    if lastState == "i":
                        totalTime += (time - lastTime).total_seconds()
            else:
                state = "n"
            lastState = state
            lastTime = time
        return totalTime


def formatTime(secs):  # 2 lines
    time_str = str(math.floor(secs / (24.0 * 60.0 * 60.0))) + " days\n"
    time_str += str(round((secs % (24 * 60 * 60)) / (60 * 60), 2)) + " hours"
    return time_str


def formatTimeOL(secs):  # one line
    time_str = str(math.floor(secs / (24.0 * 60.0 * 60.0))) + " days and "
    time_str += str(round((secs % (24 * 60 * 60)) / (60 * 60), 2)) + " hours"
    return time_str


if __name__ == "__main__":
    # root = Tk()
    print("Select the directory that the time files are located in.")
    dirname = filedialog.askdirectory()
    print("Directory: " + dirname)
    for root, dirs, filenames in os.walk(dirname):
        for f in filenames:
            totalTime = getSecs(os.path.join(root, f))
            print("Total Secs: " + str(totalTime))
            print(f.split(".")[0] + ": " + formatTimeOL(totalTime))
            print(f.split(".")[0] + ":\n" + formatTime(totalTime))
            print("\n")
