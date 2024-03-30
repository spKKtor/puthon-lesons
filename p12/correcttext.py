#pip install autocorrect
from autocorrect import Speller

spell = Speller('uk')
text = str(input('Введіть текст в якому хочети виправити помилки'))
print(spell(text))