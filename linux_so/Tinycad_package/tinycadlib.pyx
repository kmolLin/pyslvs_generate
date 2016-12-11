from libc.math cimport sqrt, sin, cos, acos
from cpython cimport bool

DEGREE = acos(-1)/180.0

cdef class Coordinate(object):

    cdef double x, y

    def __cinit__(self, x, y):
        self.x = x
        self.y = y

    cpdef public double distance(self, Coordinate obj):
        return sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)

cpdef PLLP(Coordinate A, double L0, double R0, Coordinate B, double loop=1):
    cdef:
        double x0 = A.x
        double y0 = A.y
        double x1 = B.x
        double y1 = B.y
    return (
        -loop*sqrt(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))*(-y0 + y1)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + x0 + (-x0 + x1)*(L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)/(2*sqrt((-x0 + x1)**2 + (-y0 + y1)**2)*sqrt((x0 - x1)**2 + (y0 - y1)**2)),
        loop*sqrt(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))*(-x0 + x1)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0 + (-y0 + y1)*(L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)/(2*sqrt((-x0 + x1)**2 + (-y0 + y1)**2)*sqrt((x0 - x1)**2 + (y0 - y1)**2))
    )


cpdef PLAP(Coordinate A, double L0, double a0, Coordinate B, double loop=1):
    cdef:
        double x0 = A.x
        double y0 = A.y
        double x1 = B.x
        double y1 = B.y
    return (
        -L0*loop*(-y0 + y1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-x0 + x1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + x0,
        L0*loop*(-x0 + x1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-y0 + y1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0
    )


cpdef bool legal_crank(double driver, double ground, double connect, double follower):
    # verify the fourbar is satisfied the condition
    #s + l <= p + q
    cdef:
        double tmp_driver = driver
        double tmp_ground = ground
        object fourbar
    fourbar = [driver, ground, connect, follower]
    sorted(fourbar)
    if (fourbar[0] + fourbar[3]) <= (fourbar[1] + fourbar[2]):
        # verify the fourbar is satisfied the crank condition
        if fourbar[0] == tmp_driver or fourbar[0] == tmp_ground:
            return True
    return False

#cpdef PLLP(double x0, double y0, double L0, double R0, double x1, double y1, double loop):

#    return (
#        -loop*(y1-y0)*sqrt(pow(L0,2)-pow(pow(y1-y0,2)+pow(x1-x0,2),-1)*pow(pow(R0,2)-pow(L0,2)-pow(y1,2)+2*y0*y1-pow(y0,2)-pow(x1,2)+2*x0*x1-pow(x0,2),2)/4.0)/sqrt(pow(y1-y0,2)+pow(x1-x0,2))-(x1-x0)*pow(pow(y1-y0,2)+pow(x1-x0,2),-1)*(pow(R0,2)-pow(L0,2)-pow(y1,2)+2*y0*y1-pow(y0,2)-pow(x1,2)+2*x0*x1-pow(x0,2))/2.0+x0,
#        loop*sqrt(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))*(-x0 + x1)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0 + (-y0 + y1)*(L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)/(2*sqrt((-x0 + x1)**2 + (-y0 + y1)**2)*sqrt((x0 - x1)**2 + (y0 - y1)**2))
#    )


#cpdef PLAP(double x0, double y0, double L0, double a0, double x1, double y1, double loop):
#    return (
#        -L0*loop*(-y0 + y1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-x0 + x1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + x0,
#        L0*loop*(-x0 + x1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-y0 + y1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0
#    )
