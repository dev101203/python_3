poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(poems)
 
poems_list = poems.split(',')
 
print('\n',poems_list)
 
poems_stripped = []
 
for x in poems_list:
 poems_stripped.append(x.strip())
 
print('\n',poems_stripped)
 
poems_details = []
 
for x in poems_stripped:
 
 poems_details.append(x.split(':'))
 
print('\n',poems_details)
 
titles = []
poets = []
dates = []
 
for x in poems_details:
 titles.append(x[0])
 poets.append(x[1])
 dates.append(x[2])
print('\n',poems_details)
 
for i in range(0,len(poems_details)):

    print('\n','The poem {} was published by {} in {}.'.format(titles[i], poets[i],dates[i]))
  
  

    