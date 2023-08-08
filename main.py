# Rushi Patel
from random import random,randrange

def csjob(n, gs, treatment_prob):
    '''
    n: max number of output lines
    gs: max size of a group, and assuming there are a total gs number of groups
    treatment_prob: probability of a person being treated between 0 and 1
    
    Prints out Group number, Person number, and whether they were treated or not
    '''

    # Group array populated with the group size of each group between 1 and gs inclusive
    groups=[]
    for i in range(gs):
        groups.append(randrange(1,gs+1))
    # Uncomment the line below to see the group sizes when the program testcases are run
    # print("Group sizes:",groups)

    # While the group members are not done, print the output for each person then go to the next group
    for i in range(len(groups)):
        person=1
        while groups[i] != 0:
            #If output lines are 0, exit the program
            if n==0:
                break
            # Probability check
            if random() < treatment_prob:
                print(",".join([str(i+1),str(person),"y"]))
                person+=1
            else:
                print(",".join([str(i+1),str(person),"n"]))
                person+=1
            n-=1
            groups[i]-= 1
        if n==0:
            break
    # Print out the groups that are not completed
    for i in range(len(groups)):
        if groups[i] != 0:
            print("Group",i+1,"not completed")

# Testcases

# Output lines: 9, Max  size: 3, Treatment probability: 0.3 or 30%
print("\nTestcase 1")
csjob(9,3,0.3)

# Output lines: 9, Max  size: 3, Treatment probability: 0.8 or 80%
print("\nTestcase 2")
csjob(9,3,0.8)

# Output lines: 10, Max  size: 5, Treatment probability: 0.3 or 30%
print("\nTestcase 3")
csjob(10,5,0.3)

# Output lines: 10, Max  size: 5, Treatment probability: 0.8 or 80%
print("\nTestcase 4")
csjob(10,5,0.8)