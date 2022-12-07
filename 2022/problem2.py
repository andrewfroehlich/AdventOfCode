score1,score2 = 0,0
outcomes = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6} 
outcomes2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7} 
for line in open("input2.txt"):
    score1 += outcomes[line.strip()]
    score2 += outcomes2[line.strip()]
print("Part 1: "+str(score1)+"\nPart 2: "+str(score2))