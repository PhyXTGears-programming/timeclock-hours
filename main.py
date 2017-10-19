from tkinter import filedialog

ioForm = "%H:%M:%S %d.%m.%Y"


def calcTotalTime(n):  # returns total time in seconds
    total = 0
    iLin, oLin = '', ''
    prev = 'n'
    for line in open(opts['pathTime'] + n + '.txt'):
        line = line.strip()
        lastIOA = prev[0]
        currIOA = line[0]

        if currIOA == 'i':
            iLin = line[4:]
        elif currIOA == 'o' and lastIOA != 'o' and iLin != '':
            oLin = line[4:]
            total = total + (datetime.strptime(oLin, opts['ioForm']) - datetime.strptime(iLin, opts['ioForm'])).total_seconds()
        prev = line
    return total


if __name__ == "__main__":
    # root = Tk()
    print("Select the directory that the time files are located in.")
    dirname = filedialog.askdirectory()
    print("Directory: " + dirname)
    for root, dirs, filenames in os.walk(dirname):
        for f in filenames:
            with open(os.path.join(root, f), 'r') as userFile:
                state = "o"
                # lastTime =
                for l in userFile:
                    time_str = line[4:]
                    time = datetime.strptime(time_str, ioForm)
