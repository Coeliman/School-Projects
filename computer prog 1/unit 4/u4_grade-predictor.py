exam_Total = 0
exam_List = []
print("The following 3 scores are you exam scores.")
for i in range(3):
    user_Input = int(input("Score? "))
    while user_Input > 0 and user_Input > 100:
        print("Invalid Input")
        user_Input = int(input("Score? "))
    exam_List.append(user_Input)
    exam_Total = user_Input + exam_Total
exam_Average = exam_Total / 3
print()
print("The following 4 scores are your assignment scores.")
assign_Total = 0
assign_List = []
for i in range(4):
    user_Input = int(input("Score? "))
    while user_Input > 0 and user_Input > 100:
        print("Invalid Input")
        user_Input = int(input("Score? "))
    assign_List.append(user_Input)
    assign_Total = user_Input + assign_Total
assign_Average = (assign_Total) / 4
assign_Average = assign_Average*2
overall_Score = (0.6*exam_Average)+(0.4*assign_Average)
print()
print(f"Your overall percentage is: {overall_Score}%")
print()
exam_List.sort()
examsingle_Percent = exam_List[0]/100
examfinal_Percent = examsingle_Percent*100
print(f"Your lowest exam score was {exam_List[0]}/100 - {examfinal_Percent}%.")
assign_List.sort()
assignsingle_Percent = assign_List[0]/50
assignfinal_Percent = assignsingle_Percent*100
print(f"Your lowest assignment score was {assign_List[0]}/50 - {assignfinal_Percent}%")