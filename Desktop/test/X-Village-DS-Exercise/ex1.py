import sys
sys.path.append('..')
from lib.stack import Stack

def f(dec):
    x=dec
    while x >= 1:
        rem = x % 2
        x= x//2
    # end 是让print 出来的时候是横的
        print(rem, end="")
        s.push(rem)
    
s = Stack()
f(42)
print("\n",'='*30)
f(100)





# print('Pop an item:', s.pop())
# print('Pop an item:', s.pop())
# print('Pop an item:', s.pop())
# print('Pop an item:', s.pop())
# print('Pop an item:', s.pop())
# print('Pop an item:', s.pop())


# # def dec_to_bin(dec):
# #     dec.items = 
# # (1*(2**5))
# # (0*(2**4))
# # (1*(2**3))
# # (0*(2**1))
# # (1*(2**0))
