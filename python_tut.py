# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

def sqrt(x):
    return x**(1/2);

print(sqrt(4));

name =(1,3,2,5,6);  #tuple
listin=[];
setin={1,2,3,4,5,6,4,2}
diction={"name":"bhurchtta"}


# adding elements
name=name + (2,);  # tuple immutable so need to make copy
setin.add(100);

for i in range(6):
    listin.append(i);
    print(listin[i]);

    
print("--------------------")

for i in setin:
    print(i);
    
print("--------------------")
for i in name:
    print(i);

with open("sample.csv", "w") as f:
    f.write("name,age\nAnideep,25\nJohn,30")

with open("sample.csv", "r") as f:
    print(f.read())
