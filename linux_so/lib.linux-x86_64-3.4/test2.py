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
    mechanismParams['targetPath'] = ((5 ,0),(0 ,5),(-5 ,0),(0 ,-5),)
    mechanismParams['constraint'] = [{'driver':'L0', 'follower':'L2', 'connect':'L1'},]
    mechanismParams['VARS'] = 9
    mechanismParams['formula'] = ['PLAP','PLLP']
    
    #GA Use
    #draw circle
    
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
    
    
    
