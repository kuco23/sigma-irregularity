from random import randint, random

import networkx as nx
import matplotlib.pyplot as plt

from pylib import (
    sigma, sigma_t, sigmaRatio, sigmaArgmax,
    powerAproximation,
    
    nonEdges, nonBridges,
    removeEdges, addEdges,
    
    randomConnectedEdges,
    randomConnectedGraph,
    randomTree,
    randomSigmaOptAprox,
    
    maxSigmaRatio_annealing_modified,

    localBasicNeighbor, globalBasicNeighbor,
    globalTwoPartNeighbor,
    
    neighborListToNx, nxToNeighborList, simplePlot,
)

nsim, nrange = 100, range(3, 200)
ascende = []
for i in nrange:
    startedges = i * (i - 1) // 2
    g, r = maxSigmaRatio_annealing_modified(
        i, startedges, nsim,
        globalTwoPartNeighbor
    )
    ascende.append(r)
    print(i, r)

_, c, p = powerAproximation(ascende, 0, 4, 1000, nrange)
plt.plot(nrange, ascende, 'r')
plt.plot(nrange, list(map(lambda n: c * pow(n, p), nrange)), 'g')
plt.show()
