import sys
import re

input = []
for line in sys.stdin:
	input.append(line.replace("\n",""))

number_regex = re.compile(r"(-?\d{1,3}(?:(?: \d{3})*(?:[\.,](?:\d{3} )*\d{1,3})?|\d*(?:[\.,]\d+)?)(?:(?![\.,]?\d)|(?=[\.,]\d+[\.,])))")

def convert(text):
	if number_regex.match(text):
		return float(re.sub(r"\s", '', text.replace(',','.')))
	return text
	
def split_nb(key):
	return [convert(c.lower()) for c in number_regex.split(key) if c != '' and c != None]

#Sort rely on the fact that float < string.

# Initial sort is to order entries that only differ by capital letters.
# These entries will be considered equals in the second sort and keep the same order.
for i in sorted(sorted(input), key = split_nb):
	print i