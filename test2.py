import numpy as np
import matplotlib.pyplot as plt

mystring = input('Input the numbers:')
nitrogen_numbers = input('Input the atom numbers where there is a nitrogen: ')
oxygen_numbers = input('Input the atom numbers where there is a oxygen: ')

mylist = mystring.rsplit(' ')
mylist = [int(i) for i in mylist]

dim = max(mylist)

mymat = np.zeros((dim,dim))
pertubation_nitrogen = np.zeros((dim,dim))
pertubation_oxygen = np.zeros((dim,dim))

if nitrogen_numbers != '':
    nitrogen_vector = np.zeros((1,dim))
    nitrogen_vector = nitrogen_vector[0,:]
    nitrogen_index_list = nitrogen_numbers.rsplit(' ')
    nitrogen_index_list = [int(i)-1 for i in nitrogen_index_list]

    for i in range(len(nitrogen_index_list)):
        nitrogen_vector[nitrogen_index_list[i]] = -1

    pertubation_nitrogen = np.diag(nitrogen_vector)
else:
    pass


if oxygen_numbers != '':

    oxygen_vector = np.zeros((1,dim))
    oxygen_vector = oxygen_vector[0,:]
    oxygen_index_list = oxygen_numbers.rsplit(' ')
    oxygen_index_list = [int(i)-1 for i in oxygen_index_list]

    for i in range(len(oxygen_index_list)):
        oxygen_vector[oxygen_index_list[i]] = -2

    pertubation_oxygen = np.diag(oxygen_vector)

else:
    pass



for i in range(len(mylist) - 1):

    a = mylist[i]
    b = mylist[i+1]

    if b ==0 or a==0:
        pass
    else:

        mymat[min(a,b)-1,max(a,b)-1] = -1


mymat = mymat + mymat.T

mymat += pertubation_nitrogen
mymat += pertubation_oxygen

eig, evecs = np.linalg.eig(mymat)

idx = eig.argsort()

eig = eig[idx]
evecs = evecs[:,idx]

for i in range(len(eig)):
    print('alpha + ' + str(round(-eig[i],3)) + ' beta')

print(evecs.round(2))








"""def filler(n):
    energy = 0

    if n%2 ==0:
        pairs = int(n/2)


        for i in range(pairs):
            energy += 2*eig[i]

    else:
        pairs = int((n-1)/2)

        for i in range(pairs):
            energy += 2*eig[i]

        energy += eig[pairs]

    return energy

print(filler(7))"""
