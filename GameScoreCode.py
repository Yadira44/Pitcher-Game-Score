# GSC code
# calculate game score for a pitcher using updated Tom Tango version

#start the game

pitcher_name = input("Pitcher's Name: ")
outs_recorded = int(input("Enter how many outs the pitcher recorded: "))
number_strikeouts = int(input("How many strikeouts did they accumulate: "))
hits_allowed = int(input("How many hits did they allow? "))
earned_runs = int(input("How many earned and unearned runs were allowed? "))
bb_allowed = int(input("How many walks(BB) were allowed? "))
home_runs = int(input("How many home runs were allowed? "))

#formula for game score total
Game_Score_Total = 40 + int(outs_recorded * 2) + int(number_strikeouts * 1) - int(bb_allowed * 2) - int(hits_allowed * 2) - int(earned_runs * 3) - int(home_runs * 6)

#Calculate and print the total
print(f"{pitcher_name}'s Game Score: {Game_Score_Total}")