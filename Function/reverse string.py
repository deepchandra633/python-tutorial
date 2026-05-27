s=input("Enter Any Sentence Or Words(String):")

def reverse(string):
    rev=string[::-1]
    print(rev)
reverse(s)


def rev(string):
    i=len(string)-1
    while i>=0:
        print(string[i],end="")
        i-=1
rev(s)