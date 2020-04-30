#upper,lowe case
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed )

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

## split()
line_one = "The sky has given over"

line_one_words= line_one.split()
print(line_one)
print(line_one_words)

## split the first name 
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

authors_name = authors.split(',')
print(authors_name)

## split() last name 

authors_last_name = []
for name in authors_name:
    authors_last_name.append(name.split()[-1])
print(authors_last_name)

#\n Newline , \t Horizontal Tab
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

##.join()
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

### join together the strings in the list together into a single string seperated lines
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

#.strip() removes all whitespaces in string or .strip() can delete any argument in the string '!'. not whitespaces what you want to delet you put to argument 
love_maybe = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love = []
for x in love_maybe:
    love.append(x.split())
y = '\n'.join(love_maybe)
print(love)
