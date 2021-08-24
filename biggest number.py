first=1000
second=200
third=300
fourth=400
# to find the biggest number out of four(they are not equal)
first > second, first > third, first>fourth,  'first is biggest'
second > third, second > fourth,  'second is biggest'
third > fourth, 'third is biggest'
'fourth is  biggest'
if (first > second) and (first > third) and (first > fourth):
    print("first is biggest")
elif(second > third) and (second > fourth):
    print("second is biggest")
elif(third > fourth):
    print ("third is biggest")
else:
    print(" fourth biggest")


