'''
Created on Sep 22, 2018

@author: Collin Pike
'''

if __name__ == '__main__':
    a = {'a': 'b', 'b':'c', 'd': 'b'}
    b = a.values()
    k = 0
    for i in a.values():
        for j in b:
            if(i == j):
                k += 1
            if(k > 1):
                print('too many')
        if(k > 1):
            break
        k = 0
        
        