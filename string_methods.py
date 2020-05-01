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

## .replace() 
# Replace takes two arguments and replaces all instances of the first argument in a string with the second argument. 
#there was a mistake with his last name and all instances of Toomer are lacking one o.
#Use .replace() to change all instances of Tomer in the bio to Toomer
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer','Toomer')
print(toomer_bio_fixed)

## .find()

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

# .format()
# takes variables as an argument and includes them in the string that 
# it is run on. You include {} marks as placeholders for where those variables will be imported.
def poem_title_card(poet, title):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc
print(poem_title_card('I Hear America Singing','Walt Whitman'))

##.format() 2 By including keywords in the string and in the arguments
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)



  
