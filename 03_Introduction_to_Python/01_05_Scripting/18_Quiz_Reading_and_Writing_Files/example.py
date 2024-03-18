with open("03_Introduction_to_Python/01_05_Scripting/18_Quiz_Reading_and_Writing_Files/camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())