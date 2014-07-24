from random import randint

def hsh_t1(a):
    return a%7
def hsh_t2(a):
    return a%9
def hsh_t3(a):
    return a%13

#hash table t1...mod 7
t1=[[0,None],[1,None],[2,None],[3,None],[4,None],[5,None],[6,None]]
#hash table t2...mod 9
t2=[[0,None],[1,None],[2,None],[3,None],[4,None],[5,None],[6,None],[7,None],[8,None]]
#hash table t3...mod 13
t3=[[0,None],[1,None],[2,None],[3,None],[4,None],[5,None],[6,None],[7,None],[8,None],[9,None],[10,None],[11,None],[12,None]]

def insert_t1(key,value):
    
    if t1[key][1]==None:


        t1[key][1]=value
        


    elif(type(t1[key][1])==int):


        insert_t2(hsh_t2(t1[key][1]),t1[key][1])
        
        t1[key][1]=value
        


def insert_t2(key,value):
    
    if t2[key][1]==None:


        t2[key][1]=value
        


    elif(type(t2[key][1])==int):


        insert_t3(hsh_t3(t2[key][1]),t2[key][1])
        t2[key][1]=value
        
    

def insert_t3(key,value):
    
    if t3[key][1]==None:


        t3[key][1]=value
        

    elif(type(t3[key][1])==int):

        insert_t1(hsh_t1(t3[key][1]),t3[key][1])
        
        print "Out ", t3[key][1]
        t3[key][1]=value       
        


def search(key,value):

    if t1[key][1]==value:
        print "Element found in t1"
    else:
        key=hsh_t2(value)
        if t2[key][1]==value:
            print "Element found in t2"
        else:
            key=hsh_t3(value)
            if t3[key][1]==value:
                print "Element found  in t3"
            else:
                print "Couldn't find the element"


    
for a in range(15):
    b = randint(1,100)
    print b
    insert_t1(hsh_t1(b),b)


#Searching...

element = input("Enter the element to be searched")
search(hsh_t1(element),element)
