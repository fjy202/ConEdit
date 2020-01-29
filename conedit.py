# def main(name=None):
import msvcrt,os
import sys
try:
    content=open(sys.argv[1],encoding=(sys.argv[2:] or ["gbk"])[0]).read(8191).split("\n")
    openf=True
    name=sys.argv[1]
except IndexError:
    name="untitled"
    content=['']
    openf=False
place=[0,0]
def refresh():
    os.system("cls")
    f=True
    print("\033[47;30m%s"%name,end='\033[0m\n')
    for j,V in enumerate(content):
        f=j==place[0]
        for i,v in enumerate(V):
            if j==place[0] and i==place[1]:
                f=False
                print("\033[34m|\033[0m",end="")
            print("%s"%v,end="")
        if f:
            print("\033[34m|\033[0m",end="")
        print()
refresh()
while 1:
    k=msvcrt.getwch()
    if k=='\xe0':
        k=msvcrt.getwch()
        if k=='M':
            place[1]=place[1]+1
            if place[1]>len(content[place[0]]):
                place[1]=len(content[place[0]])
        elif k=='K':
            place[1]-=1
            if place[1]<0:
                place[1]=0
        elif k=='H':
            place[0]-=1
            if place[0]<0:
                place[0]=0
            if place[1]>len(content[place[0]])-1:
                place[1]=len(content[place[0]])-1
        elif k=='P':
            place[0]+=1
            if place[0]>len(content)-1:
                place[0]=len(content)-1
            if place[1]>len(content[place[0]]):
                place[1]=len(content[place[0]])
        elif k=="S":
            if len(content)==0:
                pass
            elif content[place[0]][place[1]:]=="" and content[place[0]][place[1]:]!='':
                l=len(content[place[0]])
                content[place[0]:place[0]+2]=[content[place[0]]+content[place[0]+1]]
                if place[0]>len(content)-1:
                    place[0]=len(content)-1
                # place[1]=0
            else:
                content[place[0]]=content[place[0]][0:place[1]]+content[place[0]][place[1]+1:]
                if place[1]>len(content[place[0]]):
                    place[1]=len(content[place[0]])
    elif k=="\x03":
        sys.exit()
    elif k=="\r":
        content[place[0]:place[0]+1]=[content[place[0]][:place[1]],content[place[0]][place[1]:]]
        place[0]+=1
        place[1]=0
    elif k=="\x08":
        if place[1]<=0:
            if place[0]>0:
                ocon=content[place[0]-1]
                content[place[0]-1:place[0]+1]=[content[place[0]-1]+content[place[0]]]
                place[0]-=1
                place[1]=len(ocon)
        else:
            content[place[0]]=content[place[0]][:place[1]-1]+content[place[0]][place[1]:]
            place[1]-=1
    elif k=="\x13":
        if openf:
            open(name,"w").write("\n".join(content))
        else:
            openf=True
            name=input("filename:")
            open(name,"w").write("\n".join(content))
    else:
        if len(content)==0:
            content.append("")
        content[place[0]]=content[place[0]][0:place[1]]+k+content[place[0]][place[1]:]
        place[1]+=1
    refresh()
os.system("cls")