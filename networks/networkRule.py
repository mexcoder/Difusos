from ..memebershipFunctions.membershipFunction import MembershipFunction

class NetworkRule(object):

    def __init__(self, membershipFunction:MembershipFunction, p:float, q:float):
        # todo generate getters and setter dinamically for the properties of the MF
        self._membershipFunction = membershipFunction
        self._p = p
        self._q = q
        pass

    @property
    def membershipFunction(self):
        return self._membershipFunction
    
    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._p

    @property
    def q(self):
        return self._q
    
    @q.setter
    def q(self, value):
        self._q
    

    @property
    def m(self):
        return self._membershipFunction.c   

    @m.setter
    def m(self, value):
        self._membershipFunction.c = value

    @property
    def d(self):
        return self._membershipFunction.delta

    @d.setter
    def d(self, value):
        self._membershipFunction.delta = value
