l = int(input())
n = int(input())
for x in range(n):
    w,h=map(int,input().split())
    if(w<l or h<l):
        print("UPLOAD ANOTHER")
    elif(w==l and h==l):
        print("ACCEPTED")
    elif(w==h):
        print("ACCEPTED")
    else:
        print("CROP IT")
