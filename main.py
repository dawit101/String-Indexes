#String Indexes
#To access different parts of the string

selfish = 'me me me'
          #01234567 <-- bookself/index

print(selfish[1]) #to get the answer, start counting from the first letter as 0 (from the bookself), counting from left to right. Since 1 from the bookself is 'e', that means 'e' is the answer.

print('--------------------------')

#when using [ ] in python, you can add a start but also can add stop, [start:stop]

cat = '01234567'
      #01234567 <-- bookself

print(cat[0:3]) #the answer will be 012 because you start from 0 (from the bookself) but stop right before bookself 3, which is number 2 from the string.

print('--------------------------')

#you can also add a 'stepover' into the square brackets [start:stop:stepover]

dog = '76543210'
      #01234567 <-- bookself

print(dog[0:8:2]) #when adding 2 as the stepover, it will start from bookself 0 then skip bookself 1 to get to bookself 2.

print('--------------------------')

apple = '01234567'
        #01234567 <-- bookself
        #

print(apple[3:]) #start from bookself 3 to the end of string
print(apple[:3]) #start from bookself 0 and end before bookself 3
print(apple[::3]) #start from bookself 0 and setover to bookself 3
print(apple[-2]) #negative number means start at end of string

print('--------------------------')

#String Index Assignment

boo=  'I am PYHTON'
      #0123456789(10)

print(boo[2:4]) #find am
print(boo[2:11])  #find am PYHTON
print(boo[0:11]) #find I am PYHTON
print(boo[2:11])  #find am PYHTON
print(boo[10])  #N
print(boo[7])  #H
print(boo[0:8])  #find I am PYH
print(boo[8:11])  #find TON
print(boo[::-1]) #find NOTHYP ma I





