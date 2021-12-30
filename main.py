from tkinter.filedialog import askopenfilename
from tkinter import *
import eel, os, requests, random, emoji

eel.init('web')

emojis = [':grinning_face:', ':star:', ':dizzy:', ':collision:',
		  ':raised_hand:', ':sunglasses:', ':sparkles:', ':fire:', ':open_hands:',
		  ':cloud:', ':snowman:', ':cyclone:', ':bear:', ':paw_prints:', ':cherry_blossom:',
		  ':four_leaf_clover:', ':sunflower:', ':maple_leaf:', ':fallen_leaf:', ':mushroom:', ':palm_tree:',
		  ':seedling:', ':deciduous_tree:', ':globe_with_meridians:',
		  ':new_moon:', ':first_quarter_moon:', ':full_moon:', ':last_quarter_moon:', ':crescent_moon:',
		  ':volcano:', ':ghost:', ':sparkler:', ':bell:', ':crystal_ball:', ':camera:', ':floppy_disk:',
		  ':video_camera:', ':movie_camera:', ':telephone:', ':telephone_receiver:',
		  ':key:', ':wrench:', ':hammer:', ':money_with_wings:', ':bomb:', ':page_facing_up:',
		  ':scroll:', ':bar_chart:', ':page_with_curl:', ':clipboard:', ':open_file_folder:',
		  ':file_folder:', ':scissors:', ':pushpin:', ':books:', ':telescope:',
		  ':tennis:', ':rugby_football:', ':basketball:', ':baseball:', ':bowling:',
		  ':horse_racing:', ':trophy:', ':violin:', ':game_die:', ':pencil:', ':memo:',
		  ':microphone:', ':saxophone:', ':crown:', ':pizza:', ':meat_on_bone:',
		  ':rice_ball:', ':ice_cream:', ':tangerine:', ':cherries:', ':house:',
		  ':house_with_garden:', ':post_office:', ':school:', ':bank:', ':convenience_store:',
		  ':department_store:', ':tent:', ':factory:', ':sunrise_over_mountains:',
		  ':rainbow:', ':fountain:', ':ship:', ':airplane:', ':tram:', ':rocket:',
		  ':helicopter:', ':mountain_railway:', ':aerial_tramway:', ':oncoming_automobile:',
		  ':tractor:', ':oncoming_taxi:', ':bus:', ':articulated_lorry:', ':police_car:',
		  ':fire_engine:', ':oncoming_bus:', ':oncoming_police_car:', ':train:',
		  ':vertical_traffic_light:', ':warning:', ':construction:', ':slot_machine:',
		  ':circus_tent:', ':performing_arts:', ':round_pushpin:']


@eel.expose
def selectFolder():
	Tk().withdraw()
	location = os.system('dir')
	global choosen
	choosen = askopenfilename(initialdir=location, filetypes=[("Text files", "*.txt")])
	print(choosen)
	file = open(choosen)
	len_lines_on_file = len(file.readlines())
	eel.addText(len_lines_on_file)
	for i in range(len_lines_on_file):
		with open(choosen) as content_of_file:
			content_of_file2 = content_of_file.readlines()
			eel.addNumbers(f'+{content_of_file2[i]}')
	file.close()

@eel.expose
def getInputValue(value1, value2):
	accNamewrite = open("settings/accName.txt", mode='w')
	final_value = accNamewrite.write(value1)
	accNamewrite.close()
	tokenwrite = open('settings/token.txt', mode='w')
	final_token_value = tokenwrite.write(value2)
	tokenwrite.close()


@eel.expose
def Get_Message(Message):
	accName = open("settings/accName.txt")
	token = open('settings/token.txt')
	url = f"https://api.ultramsg.com/{accName.readline()}/messages/chat"
	file = open(choosen)
	file_len = len(file.readlines())
	for i in range(file_len):
		chosseEmoji = emoji.emojize(random.choice(emojis))
		chosseEmoji2 = emoji.emojize(random.choice(emojis))
		Final_Msg = f'{Message} {chosseEmoji} {chosseEmoji2}'
		with open(choosen) as content_of_the_file:
			phone = content_of_the_file.readlines()[i]
			payload = f"token={token.readline()}&to={phone}&body={Final_Msg}&priority=1"
			headers = {'content-type': 'application/x-www-form-urlencoded'}
			response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
			if response.status_code == 200:
				eel.Result(f'Sent to +{phone}')
				eel.Log(i + 1)
				print(f'sent to {phone}')
				print(response.text)
				eel.showLogProgramMsg(response.text)
			else:
				eel.Result(f'something wrong in: +{phone}')
				print(response.text)
				eel.showLogProgramMsg(response.text)

			eel.sleep(15.0)
	accName.close()
	token.close()
	file.close()
	eel.finshMsg()



@eel.expose
def selectImg():
	Tk().withdraw()
	location = os.system('dir')
	global choosenImg
	choosenImg = askopenfilename(initialdir=location, filetypes=[("Image", "*.JPEG *.jpg *.jpeg *.jfif *.pjpeg *.pjp *.png *.gif *.svg")])
	print(choosenImg)


@eel.expose
def Get_Message_Photo(PhotoMessage):
	accName = open("settings/accName.txt")
	token = open('settings/token.txt')
	url = f"https://api.ultramsg.com/{accName.readline()}/messages/image"
	file = open(choosen)
	file_len = len(file.readlines())
	for i in range(file_len):
		chosseEmoji = emoji.emojize(random.choice(emojis))
		chosseEmoji2 = emoji.emojize(random.choice(emojis))
		Final_Msg = f'{PhotoMessage} {chosseEmoji} {chosseEmoji2}'
		with open(choosen) as content_of_the_file:
			phone = content_of_the_file.readlines()[i]
			payload = f"token={token.readline()}&to={phone}&image=file://{choosenImg}&caption={Final_Msg}"
			headers = {'content-type': 'application/x-www-form-urlencoded'}
			response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
			if response.status_code == 200 and response.text:
				eel.Result(f'Sent to +{phone}')
				eel.Log(i + 1)
				print(response.txt)
				eel.showLogProgramMsg(response.text)
			else:
				eel.Result(f'something wrong in this phone Numbers: +{phone}')
				print(response.txt)
				eel.showLogProgramMsg(f'something wrong in this phone Numbers:{phone}')
			eel.sleep(15.0)
	accName.close()
	token.close()
	file.close()
	eel.finshMsg()

eel.start('index.html')




