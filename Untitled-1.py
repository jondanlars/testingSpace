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
print(listReverse(list))
#don't ;dslfkja;lsfj;lasjdf;lasjkdf;asdjkf;asdkjf;kasdjf
=======
print(listReverse(list));

#not sure this worked

>>>>>>> tryingThis
