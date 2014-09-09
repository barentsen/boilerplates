#!/usr/bin/env python
"""Creates a pretty plot."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from matplotlib import pyplot as plt

def simpleaxis(ax, outward=False):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    if outward:
        for loc in ['left', 'bottom']:
            ax.spines[loc].set_position(('outward', 10))
    ax.yaxis.grid(True)


if __name__ == '__main__':
    fig = plt.figure(figsize=(8, 4.5))
    simpleaxis(fig.axes[0])
    #plt.xlim([])
    #plt.ylim([])
    #plt.xticks([])
    #plt.yticks([])
    #plt.ylabel('')
    #plt.xlabel('')
    plt.tight_layout()
    plt.savefig('plot.pdf')
    plt.close()

