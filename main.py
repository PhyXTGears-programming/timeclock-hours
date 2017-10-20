from tkinter import filedialog
import os
from datetime import datetime

ioForm = "%H:%M:%S %d.%m.%Y"


# def calcTotalTime(n):  # returns total time in seconds
#     total = 0
#     iLin, oLin = '', ''
#     prev = 'n'
#     for line in open(opts['pathTime'] + n + '.txt'):
#         line = line.strip()
#         lastIOA = prev[0]
#         currIOA = line[0]
#
#         if currIOA == 'i':
#             iLin = line[4:]
#         elif currIOA == 'o' and lastIOA != 'o' and iLin != '':
#             oLin = line[4:]
#             total = total + (datetime.strptime(oLin, opts['ioForm']) - datetime.strptime(iLin, opts['ioForm'])).total_seconds()
#         prev = line
#     return total


if __name__ == "__main__":
    # root = Tk()
    print("Select the directory that the time files are located in.")
    dirname = filedialog.askdirectory()
    print("Directory: " + dirname)
    for root, dirs, filenames in os.walk(dirname):
        for f in filenames:
            with open(os.path.join(root, f), 'r') as userFile:
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
                print(f.split(".")[0] + ": " + str(totalTime))
