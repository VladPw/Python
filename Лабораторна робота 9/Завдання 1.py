import csv
import os
try:
    csvfile = open("Data.csv", "r")
    reader = csv.DictReader(csvfile, delimiter=",")
    print("Country Name: 2019 [YR2019]\n")
    for row in reader:
            value = row["2019 [YR2019]"].strip()
            if value != "" and value != "..":
                print(row["Country Name"], ": ", row["2019 [YR2019]"])
    csvfile.close()
except:
    print("Файл Data.csv не знайдено")
try:
    csvfile = open("Data.csv", "r")
    reader = csv.DictReader(csvfile, delimiter=",")
    min_v = None
    max_v = None
    min_c = ""
    max_c = ""
    for row in reader:
            value = row["2019 [YR2019]"].strip()
            try:
                num = float(value)
                if min_v is None or num < min_v:
                    min_v = num
                    min_c = row["Country Name"]
                if max_v is None or num > max_v:
                    max_v = num
                    max_c = row["Country Name"]
            except:
                continue
    os.system('cls')
    print("Country Name: 2019 [YR2019]\n")
    if min_v is not None and max_v is not None:
        print("Найнижчий показник:", min_c, ":", min_v)
        print("Найвищий показник:", max_c, ":", max_v)
        with open("Result.csv", "w", newline="") as csvfile2:
            writer = csv.writer(csvfile2, delimiter=",")
            writer.writerow(["Country Name", "2019 [YR2019]"])
            writer.writerow([min_c, min_v])
            writer.writerow([max_c, max_v])
        print("\nРезультати записані у файл Result.csv")
    else:
        print("Дані за 2019 рік відсутні або некоректні")
    csvfile.close()
except:
    print("Файл Data.csv не знайдено")