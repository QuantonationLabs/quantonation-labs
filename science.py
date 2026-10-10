"""Exact illustrative model; no archived hardware data."""
import numpy as np

def model(h=3., transverse=1.08):
    xy = np.array([(i+j/2, np.sqrt(3)*j/2) for j in range(2) for i in range(3)])
    xy -= xy.mean(0)
    d2 = ((xy[:, None]-xy[None, :])**2).sum(2)
    J = np.zeros((6,6)); mask = d2 > 1e-12; J[mask] = d2[mask]**-3
    fields = J.sum(1).mean()-h-J.sum(1)
    nn = [(i,j) for i in range(6) for j in range(i) if np.isclose(d2[i,j],1)]
    ids = np.arange(64); z = 1-2*((ids[:,None] >> np.arange(6)) & 1)
    diagonal = z@fields
    for i in range(6):
        for j in range(i): diagonal += J[i,j]*z[:,i]*z[:,j]
    H = np.diag(diagonal)
    for i in range(6): H[ids, ids^(1<<i)] = transverse
    return xy,J,fields,nn,z,H
