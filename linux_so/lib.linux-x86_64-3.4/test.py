
# from myde import build_DE
# from de2 import DiffertialEvolution


# DEGREE = math.pi/180.0
# POINT = 10


# def Length(x0, y0, x1, y1):
#     return sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0))

# def PLLP(x0, y0, L0, R0, x1, y1, loop=1):
#     # print('PLLP:',x0, y0, L0, R0, x1, y1)
#     # print(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))
#     return (
#         -loop*sqrt(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))*(-y0 + y1)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + x0 + (-x0 + x1)*(L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)/(2*sqrt((-x0 + x1)**2 + (-y0 + y1)**2)*sqrt((x0 - x1)**2 + (y0 - y1)**2)),
#         loop*sqrt(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))*(-x0 + x1)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0 + (-y0 + y1)*(L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)/(2*sqrt((-x0 + x1)**2 + (-y0 + y1)**2)*sqrt((x0 - x1)**2 + (y0 - y1)**2))
#     )


# def PLAP(x0, y0, L0, a0, x1, y1, loop=1):
#     return (
#         -L0*loop*(-y0 + y1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-x0 + x1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + x0,
#         L0*loop*(-x0 + x1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-y0 + y1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0
#     )

# def is_legal_fourbar_and_crank(driver, ground, connect, follower):
#     #s + l <= p + q
#     tmp_driver = driver;
#     tmp_ground = ground;
#     fourbar = [driver, ground, connect, follower]
#     sorted(fourbar)
#     #first if test is legal fourbar
#     if ((fourbar[0] + fourbar[3]) <= (fourbar[1] + fourbar[2])):
#         # second if test if crank
#         if (fourbar[0] == tmp_driver or fourbar[0] == tmp_ground):
#             return True;
#         else:
#             return False;
#     else:
#         return False

# def planar(v):
#     coordinates = [
#         (1,1),
#         (2,2),
#         (3,3),
#         (4,4),
#         (5,5),
#         (6,6),
#         (7,7),
#         (8,8),
#         (9,9),
#         (10,10)
#     ]

#     Ax = v[0];
#     Ay = v[1];
#     Dx = v[2];
#     Dy = v[3];
#     L0 = v[4];
#     L1 = v[5];
#     L2 = v[6];
#     L3 = v[7];
#     L4 = v[8];

#     fourbar_ground = Length(Ax, Ay, Dx, Dy)
#     fourbar_driver = L0;
#     fourbar_follower = L2;
#     fourbar_connect = L1;

#     if not is_legal_fourbar_and_crank(fourbar_driver, fourbar_follower, fourbar_connect, fourbar_ground):
#         return 1987

#     VARS = 9
#     sum = 0;
#     mx = []
#     my = []

#     for i in range(POINT):
#         try:
#             a0 = v[(VARS+i)]*DEGREE;
#             # print(Ax, Ay, L0, a0, Dx, Dy)
#             Bx, By = PLAP(Ax, Ay, L0, a0, Dx, Dy)
#             # print('B', Bx, By)
#             # print(Bx, By, L1, L2, Dx, Dy)
#             Cx, Cy = PLLP(Bx, By, L1, L2, Dx, Dy)
#             # print('C')
#             Ex, Ey = PLLP(Bx, By, L3, L4, Cx, Cy)
#             # print('E')
#         except:
#             return 1987
#         test = Length(Ex, Ey, coordinates[i][0], coordinates[i][1]);
#         if isnan(test):
#             return 1987
#         mx.append(Ex)
#         my.append(Ey)

#     for i in range(POINT - 1):
#         for j in range(POINT - 1):
#             if(Length(mx[j], my[j], coordinates[i][0], coordinates[i][1]) < Length(mx[i], my[i], coordinates[i][0], coordinates[i][1])):
#                 mx[i], mx[j] = mx[j], mx[i]
#                 my[i], my[j] = my[j], my[i]
#     for i in range(POINT - 1):
#         sum += Length(mx[i], my[i], coordinates[i][0], coordinates[i][1]);
#     if isnan(sum):
#       return 1987
#     return sum;

# if __name__ == '__main__':
    # import timeit
    # p = 10
    # var = 9
    # ub = [50] * var + [360] * p
    # lb = [-50, -50, -50, -50, 0, 0, 0, 0, 0] + [0.0] * p
    # t0 = timeit.default_timer()
    # build_DE(planar, 1, 19, 190, 0.6, 0.9, lb, ub, 1000, 100)
    # # Func, strategy, D, NP, F, CR, seed, lower, upper, maxGen, report
    # # Func, strategy, D, NP, F, CR, lower, upper, genMax, report
    # # f.run()
    # t1 = timeit.default_timer()
    # firstrun = t1 - t0

    # t0 = timeit.default_timer()
    # f = DiffertialEvolution(planar, 1, 19, 190, 0.6, 0.9, lb, ub, 1000, 100)
    # f.run()
    # # f.run()
    # t1 = timeit.default_timer()
    # print('first run', firstrun)
    # print('second run', t1 - t0)
    # f = Firefly(2, 30, 0.1, 0.2, 1, 1, [0.1,0.1], [6.0,6.0], ex3, 300, 10)
    # f.run()
    # alpha best will be 1/search scale


from planarlinkage import build_planar
from rga import Genetic
from firefly import Firefly
from de import DiffertialEvolution
if __name__ == '__main__':
    p = 10
    var = 9


    mechanismParams = dict()
    mechanismParams['Driving'] = 'A'
    mechanismParams['Follower'] = 'D'
    mechanismParams['Link'] = 'L0,L1,L2,L3,L4'
    mechanismParams['Target'] = 'E'
    mechanismParams['ExpressionName'] = 'PLAP,PLLP,PLLP'
    mechanismParams['Expression'] = 'A,L0,a0,D,B,B,L1,L2,D,C,B,L3,L4,C,E'
    mechanismParams['targetPath'] = ((1 ,1),(2 ,2),(3 ,3),(4 ,4),(5 ,5),(6 ,6),(7 ,7),(8 ,8),(9 ,9),(10,10),)
    mechanismParams['constraint'] = [{'driver':'L0', 'follower':'L2', 'connect':'L1'},]
    mechanismParams['VARS'] = 9
    mechanismParams['formula'] = ['PLAP','PLLP']

    algorithmPrams = dict()
    algorithmPrams['nParm'] = 19
    algorithmPrams['nPop'] = 250
    algorithmPrams['pCross'] = 0.95
    algorithmPrams['pMute'] = 0.05
    algorithmPrams['pWin'] = 0.95
    algorithmPrams['bDelta'] = 5.0
    algorithmPrams['upper'] = [50,50,50,50,50,50,50,50,50,] + [360.0] * p
    algorithmPrams['lower'] = [-50,-50,-50,-50, 5, 5, 5, 5, 5] + [0.0] * p
    algorithmPrams['maxGen'] = 1500
    algorithmPrams['report'] = 100
    import timeit
    t0 = timeit.default_timer()
    mechanismObj = build_planar(mechanismParams)

    f = Genetic(mechanismObj, **algorithmPrams)
    time_and_fitness, fitnessParameter = f.run()
    t1 = timeit.default_timer()
    print('total cost time: %d'%(t1-t0,))
    print(time_and_fitness)
    print(fitnessParameter)

    algorithmPrams = dict()
    algorithmPrams['D'] = 19
    algorithmPrams['n'] = 40
    algorithmPrams['alpha'] = 0.01
    algorithmPrams['betaMin'] = 0.2
    algorithmPrams['gamma'] = 1.0
    algorithmPrams['beta0'] = 1.0
    algorithmPrams['ub'] = [50,50,50,50,50,50,50,50,50,] + [360.0] * p
    algorithmPrams['lb'] = [-50,-50,-50,-50, 0, 0, 0, 0, 0] + [0.0] * p
    algorithmPrams['maxGen'] = 1500
    algorithmPrams['report'] = 100
    t0 = timeit.default_timer()
    f = Firefly(mechanismObj, **algorithmPrams)
    time_and_fitness, fitnessParameter = f.run()
    t1 = timeit.default_timer()
    print('total cost time: %d'%(t1-t0,))
    print(time_and_fitness)
    print(fitnessParameter)


    algorithmPrams = dict()
    algorithmPrams['strategy'] = 1
    algorithmPrams['D'] = 19
    algorithmPrams['NP'] = 190
    algorithmPrams['F'] = 0.6
    algorithmPrams['CR'] = 0.9
    algorithmPrams['upper'] = [50,50,50,50,50,50,50,50,50,] + [360.0] * p
    algorithmPrams['lower'] = [-50,-50,-50,-50, 0, 0, 0, 0, 0] + [0.0] * p
    algorithmPrams['maxGen'] = 1500
    algorithmPrams['report'] = 100
    t0 = timeit.default_timer()
    f = DiffertialEvolution(mechanismObj, **algorithmPrams)
    time_and_fitness, fitnessParameter = f.run()
    t1 = timeit.default_timer()
    print('total cost time: %d'%(t1-t0,))
    print(time_and_fitness)
    print(fitnessParameter)
