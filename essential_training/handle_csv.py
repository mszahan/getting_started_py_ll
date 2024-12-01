import csv

with open('10_02_us.csv', 'r') as f:
    ## in default it takes comma as delimiter
    # reader = csv.reader(f, delimiter='\t')
    ## you can read csv file like dictionary
    # reader = csv.DictReader(f, delimiter='\t')
    # for row in reader:
    #     print(row)

    data = list(csv.DictReader(f, delimiter='\t'))

primes = []
for number in range(2, 99999):
    for factor in range(2, int(number**0.5)):
        if number % factor == 0:
            break
    else:
        primes.append(number)

data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']

print(len(data))

## writing csv file

with open('10_02_ma_prime.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow([row['place name'], row['county']]) 