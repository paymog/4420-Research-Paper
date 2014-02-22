from src.ClassicQuicksort import ClassicQuicksort

__author__ = 'paymahnmoghadasian'

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,-1,-2,-4]
data.reverse()
q = ClassicQuicksort(data)

q.sort()
print q.data