## I read this problem incorrectly, and therefore stopped half way through after I realized my mistake


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def getPoints():
    thetas = np.random.rand(6) * (2*np.pi)
    xs = np.cos(thetas)
    ys = np.sin(thetas)
    return list(zip(list(xs),list(ys)))


def checkOverlap(points):


def oneIteration(points=None):
    if not points:
        points = getPoints()

    verts1 = points[0:3] + [(0.,0.)]

    verts2 = points[3:6] + [(0.,0.)]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]

    path1 = Path(verts1, codes)
    path2 = Path(verts2, codes)

    pathC = Path.circle(center=(0.,0.), radius=(1.))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    patchC = patches.PathPatch(pathC, facecolor='none', lw=2)
    ax.add_patch(patchC)

    patch1 = patches.PathPatch(path1, facecolor='orange', lw=2)
    ax.add_patch(patch1)
    patch2 = patches.PathPatch(path2, facecolor='orange', lw=2)
    ax.add_patch(patch2)


    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()
