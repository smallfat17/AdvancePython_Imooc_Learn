class O:
    pass

class A(O):
    pass

class B(O):
    pass

class C(O):
    pass

class E(A,B):
    pass

class F(B,C):
    pass

class G(E,F):
    pass

# g = G()
print(G.__mro__)