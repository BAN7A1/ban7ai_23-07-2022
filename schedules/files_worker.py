import csv
import json

with open('schedule.csv', 'w+', newline='') as csvfile:
	fieldnames = ['departure point', 'departure time',
		'destination point', 'arrival time', 'cost ticket']
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
	
	one_dict = {'departure point': 'Dnipro', 'departure time': '12:45',
		'destination point': 'Kyiv', 'arrival time': '20:30', 
		'cost ticket': '340 UAH'}
	two_dict = {'departure point': 'Lviv', 'departure time': '09:40',
		'destination point': 'Charkiv', 'arrival time': '21:14',
		'cost ticket': '576 UAH'}
	
	writer.writeheader()
	writer.writerow(one_dict)
	writer.writerow(two_dict)

with open('schedule.csv', 'r', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for i in reader:
		print(i)
		with open("schedule.json", "w+") as fh:
			json.dump(i, fh, indent=4, sort_keys=True)
