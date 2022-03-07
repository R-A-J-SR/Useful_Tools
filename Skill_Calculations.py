import math




class skill_Calculations:
    def __init__(self):
        self.self = self

    def loopingSkillHitPercentages(self):
        snum = 100
        pAmo = float(input("Please input percentage amount in decimals: "))

        timesToBeLooped = int(input("Please input how many levels to see: "))
        timeslooped = 0
        initLevel = int(input("Please input what level to start at: "))
        filename = str(input("Please enter a name for the filename: "))
        totalHits = 0
        oldtotal = 0
        while timeslooped < timesToBeLooped:
            oldnum = snum 
            newVal = snum * pAmo
            floatVal = snum + newVal
            newValRounded = int(math.ceil(floatVal))
            snum = newValRounded
            totalHits = oldtotal + newValRounded
            oldtotal = totalHits
            timeslooped += 1
            initLevel += 1
            dataInOrder = [filename, initLevel, oldnum, pAmo, floatVal, newValRounded, totalHits]
            self.saveToFile(dataInOrder)
        return filename
            

    def saveToFile(self, dataInOrder):
        with open(dataInOrder[0] + ".txt", "a") as file:
            file.write(f"At Level {dataInOrder[1]}: \n\t {dataInOrder[2]} + {dataInOrder[3]} = {dataInOrder[4]} RUP = {dataInOrder[5]} \n \t total hits = {dataInOrder[6]} \n")
            file.close()
        return

def useFunction():
    sC = skill_Calculations()
    sC.loopingSkillHitPercentages()
    print(f"Done saving data to file!\n")

useFunction()