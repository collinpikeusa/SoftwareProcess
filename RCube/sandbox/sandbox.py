'''
Created on Sep 22, 2018

@author: Collin Pike
'''

if __name__ == '__main__':
    a = []
    a.append('a')
    a.append('a')
    a.append('a')
    b = []
    b.extend(a)
    c = []
    c.append('b')
    c.append('b')
    c.append('b')
    b.extend(c)
    print(b)