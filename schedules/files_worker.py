import csv

with open('schedule.csv', 'w+', newline='') as csvfile:
	fieldnames = ['departure point', 'departure time',
		'destination point', 'arrival time', 'cost ticket']
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

	writer.writeheader()
	writer.writerow({'departure point': 'Dnipro', 'departure time': '12:45',
		'destination point': 'Kyiv', 'arrival time': '20:30', 
		'cost ticket': '340 UAH'})
	writer.writerow({'departure point': 'Lviv', 'departure time': '09:40',
		'destination point': 'Charkiv', 'arrival time': '21:14',
		'cost ticket': '576 UAH'})

with open('schedule.csv', 'r', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for i in reader:
		print(f"{['departure point']} {['departure time']}
			{['destination point']} {['arrival time']}
			{['cost ticket']}")
