def repeat_stuff(stuff,num_repeats=5):
  return stuff*num_repeats

lyrics = repeat_stuff("I want to go to USA. ", 3) + "I want to live in America . "
song = repeat_stuff(lyrics)

print(song)