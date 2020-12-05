from ..memebershipFunctions.membershipFunction import MembershipFunction

class NetworkRule(object):

    def __init__(self, membershipFunction:MembershipFunction, p:float, q:float):
        # todo generate getters and setter dinamically for the properties of the MF
        self._membershipFunction = membershipFunction
        self._p = p
        self._q = q
        pass

    def getProperties(self):
        # TODO: dinamically get all properties
        return [("p", self.__class__.p), 
                ("q", self.__class__.q),
                ("d", self.__class__.d),
                ("m", self.__class__.m)]

    @property
    def membershipFunction(self):
        return self._membershipFunction
    
    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._p = value

    @property
    def q(self):
        return self._q
    
    @q.setter
    def q(self, value):
        self._q = value
    

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
