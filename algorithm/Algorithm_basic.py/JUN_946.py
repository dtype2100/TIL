
n = int(input())
countries = {}

for i in range(n):
    country, city = input().split()
    countries[country] = city

checked_country = input()
print(countries.get(checked_country, "Unknown Country"))