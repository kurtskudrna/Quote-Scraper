import requests
from bs4 import BeautifulSoup
from random import choice

quote_list = []

response = requests.get('http://quotes.toscrape.com/').text
soup = BeautifulSoup(response, features ='html.parser')
quotes = soup.find_all(class_='quote')

for i in quotes:
	quote_list.append({
		'quote': i.span.text,
		'author': i.find(class_='author').text
		})



	
guesses = 5
single_quote = choice(quote_list)
print(single_quote['quote'])
first_initial = (single_quote['author'][0])
last_initial = (single_quote['author'].split()[1][0])
first_name = single_quote['author'].split()[0]


while guesses > 0:

	user_input = input('Guess the author of this quote? \n')



	if user_input.lower() == single_quote['author'].lower(): 
		print(f'Congrats, you got the author', single_quote['author'])
		break
	elif user_input.lower() != single_quote['author'].lower() and guesses == 5:
		print(f'That is not the author, Hint: Their first initial starts with "{first_initial}"')
		guesses -= 1
		print(f'You have {guesses} guesses left')
	elif user_input.lower() != single_quote['author'].lower() and guesses >=3:
		print(f'That is not the author, Hint: Their initials are "{first_initial}, {last_initial}"')
		guesses -= 1
		print(f'You have {guesses} guesses left')
	elif user_input.lower() != single_quote['author'].lower() and guesses >=1:
		print(f'That is not the author, Hint: Their first name and last initial are "{first_name}, {last_initial}"')
		guesses -= 1
		print(f'You have {guesses} guesses left')

if guesses == 0:
	print('Game over, you are out of guesses')
	print(f'The author was', single_quote['author'])







