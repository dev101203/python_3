highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# first structure
print(highlighted_poems)

#2 create substring 
highlighted_poems_list = highlighted_poems.split(',')
print('\n', highlighted_poems_list)

#4 remove all the whitespaces
highlighted_poems_stripped = []
for x in highlighted_poems_list:
  highlighted_poems_stripped.append(x.strip('  '))
print('\n',highlighted_poems_stripped) 

#5 break up all the information for each poem into it’s own list and split each string around the : characters and append the new lists into
highlighted_poems_details = []
for x in highlighted_poems_stripped:
  highlighted_poems_details.append(x.split(':'))
print('\n',highlighted_poems_details)

#6separate out all of the titles, the poets, and the publication dates into their own lists.
titles = []
poets = []
dates = []
for x in highlighted_poems_details:
 titles.append(x[0])
 poets.append(x[1])
 dates.append(x[2])
print('\n',highlighted_poems_details)

for i in range(0,len(highlighted_poems_details)):
  print('\n','The poem {} was published by {} in {}.'.format(titles[i],poets[i],dates[1]))









