import csv

with open("17_sign_ups.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_sign_uos.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)
