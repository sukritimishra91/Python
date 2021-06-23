# dictionaries
csv_file = "file-name" 
class scores = {}

with open(file-name, as "r") as f:
  for line in f:
  print(repr(line))
  date, classname, score = line.strip().split(",")
  print(date, classname, score)
  class_scores[classname] = class_scores.get(classname, 0) + int(score)
  output_file = "results.txt"
    with open(output_file, "w") as f:
    	for classname, score in class_scores.items():
    		f.write(f"{classname}, {score}\n")



    		




