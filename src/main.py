from itertools import chain
import time

#stoc function from array of string
def stoc(array):
    res = list(chain.from_iterable(array))
    return res

#delete duplicate char function from array
def delDupc(array):
    tmparr = []
    for i in array:
        if i not in tmparr:
            tmparr.append(i)
    return tmparr

#mfungsi memasukkan opperand ke array operand
def insopp(arrayopp,arrayawal):
    for i in range(len(arrayawal)-1):
        arrayopp.append(arrayawal[i])

#prosedur permutasi (bad code banget)
def permutasi(cobainaja,ArrPerm):
    if cobainaja <= 10:
        for i in range(10):
            for j in range(10):
                if i != j :
                    if cobainaja != 2:
                        for k in range(10):
                            if k != i and k != j :
                                if cobainaja != 3:
                                    for l in range(10):
                                        if l != i and l != j and l !=k:
                                            if cobainaja !=4:
                                                for m in range(10):
                                                    if m != i and m !=j and m != k  and m != l:
                                                        if cobainaja !=5:
                                                            for n in range(10):
                                                                if n != i and n != j and n!= k and n != l and n != m:
                                                                    if cobainaja != 6:
                                                                        for o in range(10):
                                                                            if o != i and o != j and o != k and o != l and o != m and o != n :
                                                                                if cobainaja != 7:
                                                                                    for p in range(10):
                                                                                        if p != i and p != j and p != k and p != l and p != m and p != n and p != o :
                                                                                            if cobainaja != 8:
                                                                                                for q in range(10):
                                                                                                    if q != i and q != j and q != k and q != l and q != m and q != n and q != o and q != p:
                                                                                                        if cobainaja != 9:
                                                                                                            for r in range(10):
                                                                                                                if r != i and r != j and r != k and r != l and r != m and r != n and r != o and r !=p and r != q :
                                                                                                                    ArrPerm += [[i,j,k,l,m,n,o,p,q,r]]
                                                                                                        else:
                                                                                                            ArrPerm += [[i,j,k,l,m,n,o,p,q]]

                                                                                            else:#8
                                                                                                ArrPerm += [[i,j,k,l,m,n,o,p]]
                                                                                else:#7
                                                                                    ArrPerm += [[i,j,k,l,m,n,o]]
                                                                    else:#6
                                                                        ArrPerm += [[i,j,k,l,m,n]]
                                                        else:#5
                                                            ArrPerm += [[i,j,k,l,m]]
                                            else:#4
                                                ArrPerm += [[i,j,k,l]]
                                else:#3
                                    ArrPerm += [[i,j,k]]
                    else: #2
                        ArrPerm += [[i,j]]
    else:#hadle kasus >10
        print("Karakter unik terlalu banyak (>10)")

#fungsi mencari index character di array char unik
def findcidx(char,arrayunik):
    found = False
    i = 0
    while not(found) and i < len(arrayunik) :
        if arrayunik[i] == char :
            found = True
        else:
            i += 1
    return i       

# prosedur mencari solusi
def isEqual(opperand,result,unik,ArrPerm,solusi,countfail):
    tambah = 0
    anssum = 0
    firstcans = result[0][0]
    firstc = []
    for i in range(len(opperand)):
        for c in range(len(opperand[i])):
            if c == 0 :
                firstc.append(opperand[i][c])
            tambah += ArrPerm[findcidx(opperand[i][c],unik)]*10**(len(opperand[i])-c-1)

    for c in range(len(result[0])):
        anssum += ArrPerm[findcidx(result[0][c],unik)]*10**(len(result[0])-c-1)
    

    if tambah == anssum :
        firstintans = ArrPerm[findcidx(result[0][0],unik)]
        firstint = []
        #handle huruf depan = 0
        for i in range(len(firstc)):
            firstint.append(ArrPerm[findcidx(firstc[i],unik)])
        if checkzero(firstint) == False :
            if firstintans != 0 :
                solusi.append(ArrPerm)
    else:
        countfail[0] += 1 
        
def checkzero(array):
    found = False
    i = 0
    while not(found) and i < len(array):
        if array[i] == 0:
            found = True
        else:
            i += 1
    
    if found == True :
        return True
    else :
        return False

#open and read file
filename = input("Tuliskan nama file dengan extensinya (contoh.txt) :")
print("Mohon tunggu sedang diproses...\n")
f = open(filename, "r")
isi = f.readlines()

#add to a list (alphabet only)
start_time = time.time()
arrAwal = []
#arrAwalv2 = []
for i in range(len(isi)):
#    arrAwalv2.append(isi[i].rstrip('\n'))
    arrAwal.append(isi[i].rstrip('\n').rstrip('+').replace(" ",""))
savesign = []
savesign.append(arrAwal[len(arrAwal)-2])
del arrAwal[len(arrAwal)-2]


#global variable &  inisiasi array
ArrPerm = []
arrNumber = []
opperand = []
result = []
solusi = []
countfail = [0]
#element result diisi dengan result di file
result.append(arrAwal[len(arrAwal) -1])

#operand diisi ke array ooperand 
insopp(opperand,arrAwal)

#make array of huruf unik
huruf = stoc(arrAwal)
unik = delDupc(huruf)

# main driver
panjangunik = len(unik)
permutasi(panjangunik,ArrPerm)
for i in range(len(ArrPerm)):
    isEqual(opperand,result,unik,ArrPerm[i],solusi,countfail)

#print soal
#for i in range(len(arrAwalv2)):
#    print(arrAwalv2[i])
for i in range (len(opperand)):
    tempstr = str(opperand[i])
    if(i == len(opperand) -1):
        print(tempstr.rjust(8),end="+\n")    
    else:
        print(tempstr.rjust(8))
tempstr = str(savesign[0])
print(tempstr.rjust(8))
tempstr = str(result[0])
print(tempstr.rjust(8))
print("")
#print solusi
print ("solusi : \n")
if(len(solusi) != 0):
    for ans in range(len(solusi)):
        tambah = 0
        anssum = 0
        for i in range(len(opperand)):
            for c in range(len(opperand[i])):
                tambah += solusi[ans][findcidx(opperand[i][c],unik)]*10**(len(opperand[i])-c-1)
            if i == len(opperand)-1:
                strnum = str(tambah)
                print(strnum.rjust(8),end="+\n")
            else:
                strnum = str(tambah)
                print(strnum.rjust(8))
            tambah = 0
        tempstr=str(savesign[0])
        print(tempstr.rjust(8))
        for c in range(len(result[0])):
            anssum += solusi[ans][findcidx(result[0][c],unik)]*10**(len(result[0])-c-1)
        anssnum = str(anssum)
        print(anssnum.rjust(8))
        print("")
else:
    print("No solution\n")

print("Number of Tries : ", countfail[0], end=" tries ")
print("from", len(ArrPerm), "possibility")
print("Execution time :  %.3f seconds" % (time.time() - start_time))
input("Press Enter to EXIT. ")