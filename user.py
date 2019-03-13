from sense_hat import SenseHat
import time 

import requests
import json
sense = SenseHat()

sense.clear()


def loadUser():
	global name
	
	data = requests.get('https://randomuser.me/api/').content
	j = json.loads(data)
	name = j['results'][0]['name']['first']
	sense.show_message(name, text_colour=[255, 255, 255])
	return name

loadUser()

def like():
	person = {'naam: ': name, 'status: ': 'like'}
	with open('data.json', 'w') as outfile:
				json.dump(person, outfile)
	loadUser()

				
	sense.clear()

def dislike():
	person = {'naam: ': name,'status: ': 'dislike'}
	with open('data.json', 'w') as outfile:
				json.dump(person, outfile)
	
	loadUser()

				
	sense.clear()

try:
	while('true'):
		event = sense.stick.wait_for_event()


		if event.direction == 'left' and event.action == 'pressed':
			time.sleep(0.5)
			dislike()
			print('dislike')
						
		elif event.direction == 'right' and event.action == 'pressed':
			time.sleep(0.5)
			like()
			print('like')

except (KeyboardInterrupt, SystemExit):
    print('bliep bloep,  you are out')
    sense.clear()
    sys.exit(0)

