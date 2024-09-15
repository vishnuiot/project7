import csv

with open('list1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Journal_name", "Impactfactor", "University_name", "Lat","Long"]
    
    writer.writerow(field)
    writer.writerow(["arixiv.org", "9.1", "university of chicago","41.789722", "-87.599724"])
    