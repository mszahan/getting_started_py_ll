import statistics

ages_data = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(ages_data))
print(statistics.mode(ages_data))
print(statistics.median(ages_data))

print(statistics.variance(ages_data))
## standard deviation is the square root of variance
print(statistics.stdev(ages_data))
