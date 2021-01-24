from itertools import chain
import time

#open and read file
f = open("test.txt", "r")
isi = f.readlines()

#add to a list (alphabet only)
arrAwal = []
for i in range(len(isi)):
    arrAwal.append(isi[i].rstrip('\n').rstrip('+'))
del arrAwal[len(arrAwal)-2]

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


def insopp(arrayopp,arrayawal):
    for i in range(len(arrayawal)-1):
        arrayopp.append(arrayawal[i])

def arrangka(count):
    tempoarr = []
    for i in range(count):
        tempoarr.append(i)
    #[0,1,2,3,...,(len(arrayunik))]
    return tempoarr

def permutasi(listangka): 
    # isEmpty
    if len(listangka) == 0: 
        return [] 
  
    # isOneElmt
    if len(listangka) == 1: 
        return [listangka] 
    
    # len(listangka) > 1
    temparray = []

    for i in range(len(listangka)): 
       element = listangka[i] 
       sisa = listangka[:i] + listangka[i+1:] 
       for perm in permutasi(sisa): 
           temparray.append([element] + perm) 
    return temparray 

def findcidx(char,arrayunik):
    found = False
    i = 0
    while not(found) and i < len(arrayunik) :
        if arrayunik[i] == char :
            found = True
        else:
            i += 1

    return i       

#global variable &  inisiasi array


arrNumber = []
opperand = []
result = []
solusi = []
#element result diisi dengan result di file
result.append(arrAwal[len(arrAwal) -1])
#operand diisi ke list ooperand 
insopp(opperand,arrAwal)

#make array of huruf unik
huruf = stoc(arrAwal)
unik = delDupc(huruf)

# print(opperand)
# print(result)
# print(unik)


#cari solusi
def isEqual(opperand,result,unik,ArrPerm,solusi):
    tambah = 0
    anssum = 0
    #[SEND,MORE]
    for i in range(len(opperand)):
        for c in range(len(opperand[i])):
            # print(sum)
            tambah += ArrPerm[findcidx(opperand[i][c],unik)]*10**(len(opperand[i])-c-1)
           # print(tambah,ArrPerm,opperand[i])

    for c in range(len(result[0])):
        # print(anssum)
        anssum += ArrPerm[findcidx(result[0][c],unik)]*10**(len(result[0])-c-1)
        # print(anssum,ArrPerm,result[0])
    
    # if tambah != 10652 and anssum == 10652 :
    #     print(ArrPerm)
    #     print(tambah)
    #     print(anssum)
    # if tambah == 10652 and anssum != 10652 :
    #     print(unik)
    #     print(ArrPerm)
    #     print(tambah)
        # print(anssum)
    if tambah == anssum :
        solusi.append(ArrPerm)
        #sprint(solusi)

# main driver
#isi array angka sesuai panjang isi array huruf unik
arrNumber = arrangka(len(unik))
array = arrNumber


indexarray = len(unik)
while indexarray > 0 :
    for j in range(10-len(unik)):
        ArrPerm = []
        for isilist in permutasi(array): 
            ArrPerm.append(isilist)
        for i in range(len(ArrPerm)):
            isEqual(opperand,result,unik,ArrPerm[i],solusi)
        #ambil element akhir arrayNumber inc
        print(arrNumber)
        arrNumber[indexarray-1] += 1
        print(arrNumber)
    indexarray -= 1

#dia udah di index akhir



def permutasii(n):
    for j in range(10):
        if  :
            permutasii(n-1)

            