import random


def helloWorld():
  languages = ['Hallo Welt', 'Hello World', 'ciao mondo', 'hallo verden', 'hola mundo', 'Bonjour le monde']
  randomNumber = random.randint(1, 10)
  print(languages[randomNumber])



helloWorld()
