import csv

def writeTallyScore(file_name):
	
	tally_scores = {}

	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if row[1] in tally_scores:
				tally_scores[row[1]] = tally_scores[row[1]] + int(row[2])
			else:
				tally_scores[row[1]] = int(row[2])

	with open('results.txt', mode='w') as output_file:
		writer = csv.writer(output_file, delimiter=',')
		for klass in tally_scores:
			writer.writerow([klass, tally_scores[klass]])

writeTallyScore('input.txt')

