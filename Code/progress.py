# -*- coding: utf-8 -*-

import time

def progress(frac, tic=-1):
    # fancy function to follow progression. to disable it, comment
    # lines 55, 58, 59
    if tic == -1:
        # just some fancy things to follow progression
        print("\033[2K" + str(round(100*frac, 1)) + "%" + '[' +
              round(20*frac)*'='+(20-round(20*frac))*' ' +']', end='\r')
    else:
        # just some fancy things to follow progression
        toc = time.perf_counter()
        mi = str(int((toc-tic)/60))
        sec = str(int((toc-tic) - 60*int(mi)))
        if frac == 0:
            left = 1000
        else:
            left = round((toc-tic)/frac - (toc-tic))
        mi_left = str(int((left/60)))
        sec_left = str(int(left - 60*int(mi_left)))
        if len(sec) == 1:
            sec = '0' + sec
        if len(sec_left) == 1:
            sec_left = '0' + sec_left
        print("\033[2K" + str(round(100*frac, 1)) + "%" + '[' +
              round(20*frac)*'='+(20-round(20*frac))*' ' +']' +
              ' ' + mi + ':' + sec + ' Time left : ' + mi_left + ':'+sec_left + ' ', end='\r')

