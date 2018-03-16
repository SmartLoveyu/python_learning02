list = ['Haking','Max','Einstein','Elizabeth']
print("I would like to invite " + list[0] +" ," + list[1] +" ," + list[2] +" and " +list[3] + " to dinner!")
print("\nBut I just learned that " + list[1] + " can't keep the appiontment")

list[1] = 'newton'
print("\nSo I also invite " + list[1].title() + " to the dinner")

print("So, finally. I would like to invite " + list[0] +" ," + list[1].title() +" ," + list[2] +" and " +list[3] + " to the dinner!")

print("This time, T find a bigger table, so I can invite more person!")
list.insert(0,'maxwell')
list.insert(2,'pinker')
list.append('smart')

print("So, finally. I would like to invite " + list[0].title() +" ," + list[1].title() +" ," + list[2].title() +" ," +list[3].title() + list[4].title() +" ," + list[5].title() +" and " +list[6].title() + " to the dinner!")
print("But the new table can't arrive on time, so I have to invite only two person....")

sorry = list.pop()
print("\nHi, " + sorry.title() + ". I can't invite you to dinner....")
sorry = list.pop()
print("\nHi, " + sorry.title() + ". I can't invite you to dinner....")
sorry = list.pop()
print("\nHi, " + sorry.title() + ". I can't invite you to dinner....")
sorry = list.pop()
print("\nHi, " + sorry.title() + ". I can't invite you to dinner....")
sorry = list.pop()
print("\nHi, " + sorry.title() + ". I can't invite you to dinner....")
print(list)

print("\nLuckly, " + list[0] + ", I can still invite you!")
print("Luckly, " + list[0] + ", I can still invite you!")

del list[0]
del list[0]
print(list)
print("happy dinner!")
