#import time between the questions
import time 

#Choice_1
print("You wake up you realise that youre late for school, what do you do, stay in bed? or get up ?")
choice_1 = input()
if choice_1 == 'get up':
    print("You get out of bed and rush to school!")
elif choice_1 == 'stay in bed':
    print("You do not give a shit and go back to sleep.")
else:
    print(choice_1, " wasn't a valid choice")
time.sleep(3)

#Choice_2
print("you finnaly arrived at school but the hour is almost over, what do you do, go to the lesson ? or wait for the next lesson to start ?")
choice_2 = input()
if choice_2 == 'go to the lesson':
    print("You walk up the stairs and the bell rings the lesson is over what a waste of time.")
elif choice_2 == 'wait for the next lesson to start':
    print("your really sleepy and regret going to school as the lesson goes on you fall asleep again.")
else:
    print(choice_2, " wasn't a valid choice")
time.sleep(3)

#Choice_3
print("Your alarm rings, do you GETUP or SNOOZE ?")
choice_3 = input()
if choice_3 == 'GETUP':
    print("You get out of bed and feel fresh!")
elif choice_3 == 'SNOOZE':
    print("Hmmmmmm zzzzzzzzzzzzzzzzzzzzzzzzzz")
else:
    print(choice_3, " wasn't a valid choice")

#Choice_4
print("Your alarm rings, do you GETUP or SNOOZE ?")
choice = input()
if choice == 'GETUP':
    print("You get out of bed and feel fresh!")
elif choice == 'SNOOZE':
    print("Hmmmmmm zzzzzzzzzzzzzzzzzzzzzzzzzz")
else:
    print(choice, " wasn't a valid choice")

#Choice_5
print("Your alarm rings, do you GETUP or SNOOZE ?")
choice = input()
if choice == 'GETUP':
    print("You get out of bed and feel fresh!")
elif choice == 'SNOOZE':
    print("Hmmmmmm zzzzzzzzzzzzzzzzzzzzzzzzzz")
else:
    print(choice, " wasn't a valid choice")