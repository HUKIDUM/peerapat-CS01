A=int(input('คะแนนเก็บ = '))
A<30
B=int(input('คะแนนสอบกลางภาต = '))
B<30
C=int(input('คะแนนสอบปลายภาต = '))
C<40
D=A+B+C
if(80<=D<=100):
    print('A')
elif(75<=D<=79):
    print('B+')
elif(70<=D<=74):
    print('B')
elif(65<=D<=69):
    print('C+')
elif(60<=D<=64):
    print('C')
elif(55<=D<=59):
    print('D+')
elif(50<=D<=54):
    print('D')
else:
    print('F')