<<<<<<< HEAD
print("hello");
=======
>>>>>>> bfa49f03000823de57d21b58eefa70cc01a8095c
#function to find sum of the elements of a list
def listAdd(list):
    sum = 0;
    for i in range(len(list)):
        sum = sum + list[i];
    return sum;

#function to find product of the elements of a list
def listProd(list):
    prod = 1;
    for i in range(len(list)):
        prod *= list[i];
    return prod;

#function to reverse list elements
def listReverse(list):
    revList = list;
    revList.reverse();
    return revList;

#main code
list = [1,2,4,5,6];

#Print out the results
print("List is:");
print(list);
print("Sum of elements is: " + str(listAdd(list)));
print("Product of elements is: " + str(listProd(list)));
print("The list reversed:");
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
print(listReverse(list))
#don't ;dslfkja;lsfj;lasjdf;lasjkdf;asdjkf;asdkjf;kasdjf
#i just want this to work
=======
print(listReverse(list))
#don't ;dslfkja;lsfj;lasjdf;lasjkdf;asdjkf;asdkjf;kasdjf
>>>>>>> bfa49f03000823de57d21b58eefa70cc01a8095c
=======
print(listReverse(list));

#not sure this worked

<<<<<<< HEAD
>>>>>>> 2c32e31 (removed inputs)
=======
print(listReverse(list))
#don't ;dslfkja;lsfj;lasjdf;lasjkdf;asdjkf;asdkjf;kasdjf
>>>>>>> 2f45137 (jhjjjkl)
=======
>>>>>>> tryingThis
>>>>>>> bfa49f03000823de57d21b58eefa70cc01a8095c
