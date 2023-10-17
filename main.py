# import the random module
import random
import math

# Vars
songs_list = list(range(1, 3001))
played_songs = []
favorite_songs_played= 0
plays = 3000
plays_song_output = []
ending = ""
final_output = "Song Number,Favorite Song"

for r in range(plays):
    for i in range(5):
        random.shuffle(songs_list)
    # print("\nAfter the shuffles : ")
    # print(songs_list)
    played_songs.append(songs_list[0])
print(f"\nthe songs played were:\33[90m \33[7m\n-------------------")
for i in played_songs:
    song_extention = ""
    song_extention_csv = "no"
    if i<51 :
        favorite_songs_played = favorite_songs_played + 1
        song_extention = "Favorite song"
        song_extention_csv = "yes"
    num_lengh = 1 + math.floor(math.log10(i))
    if num_lengh < 4:
        if num_lengh == 3:
            song_extention = " "
        elif num_lengh == 2:
            if song_extention != "Favorite song":
                song_extention = "  "
        elif num_lengh == 1:
            song_extention = " " + song_extention
            if song_extention != " Favorite song":
                song_extention = "  "
    if song_extention != "Favorite song":
        if song_extention != " Favorite song":
            song_extention = f"{song_extention}           "
    plays_song_output.append(f"#{i},{song_extention_csv}")
    print(f"\33[31m \33[7m#{i} {song_extention} \33[0m\33[90m \33[7m\n-------------------")
if favorite_songs_played == 0:
    print("\n\nno favorite songs were played")
else:
    print(f"\33[0m\n\n{favorite_songs_played} favorite songs were played")
chance = favorite_songs_played / plays
print(f"\33[0mchance of a favorite song playing:\n\33[31m\33[7m{chance}\33[0m (\33[31m\33[7m{favorite_songs_played} out of {plays}\33[0m)")
# file_number = 0
try:
    txt = open(f"output.csv", "w")
except:
    txt = open(f"output.csv", "x", "w")
#try:
#    py = open("output.py")
#except:
#    py = open("output.py", "x")
for i in plays_song_output:
    final_output = final_output + "\n" + i
txt.write(final_output)