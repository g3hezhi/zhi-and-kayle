N = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500]
from scipy import stats

def createIncreArff(arffile):
    with open(arffile) as f:
        strlist = f.read().strip().split("\n")
    print(len(strlist))
    for i in N:
        outf = open("arff_"+str(i)+".arff",'w+')
        const = strlist[0:27]
        post  = strlist[28:28+i]
        nega  = strlist[5528:5528+i]
        allx = const+post+nega
        for j in allx:
            outf.write(j+"\n")
    outf.close()
    f.close()
    
    
def createCross(arffile,index):
    with open(arffile) as f:
        strlist = f.read().strip().split("\n")
    const = strlist[0:27]
    const1 = strlist[0:27]
    part1 = strlist[28:28+550]+strlist[5528:5528+550]
    part2 = strlist[28+550*1:28+550*2]+strlist[5528+550*1:5528+550*2]
    part3 = strlist[28+550*2:28+550*3]+strlist[5528+550*2:5528+550*3]
    part4 = strlist[28+550*3:28+550*4]+strlist[5528+550*3:5528+550*4]
    part5 = strlist[28+550*4:28+550*5]+strlist[5528+550*4:5528+550*5]
    part6 = strlist[28+550*5:28+550*6]+strlist[5528+550*5:5528+550*6]
    part7 = strlist[28+550*6:28+550*7]+strlist[5528+550*6:5528+550*7]
    part8 = strlist[28+550*7:28+550*8]+strlist[5528+550*7:5528+550*8]
    part9 = strlist[28+550*8:28+550*9]+strlist[5528+550*8:5528+550*9]
    part10 = strlist[28+550*9:28+550*10]+strlist[5528+550*9:5528+550*10]
    a = [part1,part2,part3,part4,part5,part6,part7,part8,part9,part10]
    traindata = const
    for i in range(len(a)):
        if i != index:          
            traindata += a[i]
    outf1 = open("3.4files/test_"+str(index)+".arff",'w')
    outf2 = open("3.4files/train_"+str(index)+".arff",'w')
    for j in const1+a[index]:
        outf1.write(j+"\n")        
    for k in traindata:
        outf2.write(k+"\n")
    outf1.close()
    outf2.close()
    f.close()
BAYE = [[279,271,172,378],[244,306,174,376],[262,288,162,388],[278,272,182,368],[264,286,177,373],[268,282,171,379],[294,256,210,340],[299,251,206,344],[274,276,177,373],[261,289,165,354]]
SMO = [[327,223,187,363],[344,206,232,318],[342,208,207,343],[342,208,225,325],[347,203,222,328],[334,216,219,331],[354,196,231,319],[339,211,220,330],[342,208,215,335],[337,213,204,345]]
TREE =[[324,226,197,353],[318,232,236,314],[333,217,233,317],[303,247,219,331],[311,239,224,326],[337,213,235,315],[322,228,243,307],[347,203,246,304],[319,231,238,312],[299,251,226,323]]
def calA(a1,b1,a2,b2):
    return (float(a1+b2))/(float(a1+a2+b1+b2))*100
def calP(a,b,c,d):
    return (float(a/float((a+c)))*100,float(b/(float(b+d)))*100)
def calR(a,b,c,d):
    return (float(a/(float(a+b)))*100,float(d/(float(c+d)))*100)

def allA(b,s,t):
    answer = []
    bayeA = []
    smoA = []
    treeA = []
    bayeP = []
    smoP = []
    treeP = []
    bayeR = []
    smoR = []
    treeR = []    
    for i in b:
        bayeA.append(calA(i[0],i[1],i[2],i[3]))
        bayeP.append(calP(i[0],i[1],i[2],i[3]))
        bayeR.append(calR(i[0],i[1],i[2],i[3]))
    for i in s:
        smoA.append(calA(i[0],i[1],i[2],i[3]))
        smoP.append(calP(i[0],i[1],i[2],i[3]))
        smoR.append(calR(i[0],i[1],i[2],i[3]))        
    for i in t:
        treeA.append(calA(i[0],i[1],i[2],i[3]))
        treeP.append(calP(i[0],i[1],i[2],i[3]))
        treeR.append(calR(i[0],i[1],i[2],i[3]))        
    answer.append(bayeA)
    answer.append(bayeP)
    answer.append(bayeR)
    answer.append(smoA)
    answer.append(smoP)
    answer.append(smoR)
    answer.append(treeA)
    answer.append(treeP)
    answer.append(treeR)
    print("BAYE SMO TREE")
    return answer

def writeF(answer):
    outf = open("3.4output.txt",'w+')
    for i in answer:
        outf.write("line\n")
        for j in i:
            outf.write(str(j)+"\n")
    outf.close()
    
def compare(a,b):
    s = stats.ttest_rel(a,b)
    return s
    
