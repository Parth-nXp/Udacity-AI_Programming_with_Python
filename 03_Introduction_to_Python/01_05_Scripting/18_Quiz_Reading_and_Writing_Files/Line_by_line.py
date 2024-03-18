camelot_lines = []
with open("03_Introduction_to_Python/01_05_Scripting/18_Quiz_Reading_and_Writing_Files/camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)