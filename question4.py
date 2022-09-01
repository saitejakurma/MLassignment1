#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of Set it_companies:",len(it_companies))
#add(elements) adds elements into the set
it_companies.add('Twitter')
print("it_companies: ", it_companies)
it_companies.update(['Cognizant','LinkedIn','Salesforce','Wipro'])
print("it_companies after update: ",it_companies)
#remove() remove the element from the set
it_companies.remove("LinkedIn")
print(it_companies)

#Difference between remove and discard
print("\nDifference between Remove() and Discard(): Discard() method is different from the remove() method, because the remove() method will throw an error if the specified item is not present in list, whereas the discard() method will not throw any error if item doesn't exist in list.")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#all set operation can be performed in set: union(), intersection()
print("\nUnion of A and B sets: ",A.union(B))
print("Intersection of A and B sets: ",A.intersection(B))
#issubset() returns true if it is subset of other else false
print("A is Subset of B? ",A.issubset(B))
#to check is A and B are disjoint sets ( no elements in common)
print("A and B are disjoint sets? ",A.isdisjoint(B))
print("(AUB) AND (BUA): ",(A.union(B)).intersection(B.union(A)))
#checking symmetric differece .. return the extra elements of set A that are not in B
print("Symmetric Difference of A with B: ",A.symmetric_difference(B))
#clear() clear/ delete all elements from set
A.clear()
B.clear()
print("After clear Set A values: ", A,"\tSet B values: ",B)

age = [22, 19, 24, 25, 26, 24, 25, 24]
print("\nage list: ",age)
age_set = set(age)
print("set of ageslist: ", age_set)
print("Length of age list: ", len(age), "\nLength of age set",len(age_set))