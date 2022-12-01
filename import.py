import requests
import re

url = 'https://adventofcode.com/2022/day/1/input'
r = requests.get(url)
data = r.text
print(data)
