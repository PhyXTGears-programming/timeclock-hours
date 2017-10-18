from tkinter import filedialog
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename

if __name__ == "__main__":
    # root = Tk()
    print("Select the directory that the time files are located in.")
    dirname = filedialog.askdirectory()
    print("Directory: " + dirname)
    for root, dirs, filenames in os.walk(dirname):
        for f in filenames:
            with open(os.path.join(root, f), 'r') as userFile:
                state = "o"
                lastTime = 
                for l in userFile:
                    #
