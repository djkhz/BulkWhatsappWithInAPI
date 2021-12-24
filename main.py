from tkinter.filedialog import askopenfilename
from tkinter import *
import eel, os

eel.init('web')
@eel.expose
def selectFolder():
	Tk().withdraw()
	location = os.system('dir')
	choosen = askopenfilename(initialdir=location, filetypes=[("Text files", "*.txt")])
	print(choosen)
	file = open(choosen)
	len_lines_on_file = len(file.readlines())
	eel.addText(len_lines_on_file)
	for i in range(len_lines_on_file):
		with open(choosen) as content_of_file:
			content_of_file2 = content_of_file.readlines()
			eel.addNumbers(content_of_file2[i])
	file.close()

eel.start('index.html')








