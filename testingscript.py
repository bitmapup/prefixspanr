#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Lock
import copper.prefixspan as ps
import copper.fileprocessor as fp
import time
import sys
import math
sys.setrecursionlimit(10000)
import utils

def analyze(infile, outfile, options):
    u_db = open(infile, 'r')
    s_db = fp.readDB(u_db, options)

    
    options['threshold']=int(math.ceil(options['threshold']*len(s_db)))
    start = time.time()
    res = ps.prefixspan(s_db, options)

    end = time.time()
    out = open(outfile,'w')
    out.write("Options: "+str(options)+'\n')
    out.write("Patterns Found: " + str(len(res))+'\n')
    out.write("Time Taken: " + str(end - start)+'\n')
    for pat in sorted(res, key=lambda x: x[1]):
        out.write(str(pat)+'\n')
    out.close()
    return

"""
if __name__ == '__main__':
    #infile = 'C01T5S250I003SP5.txt'
    #infile = 'Test.txt'
    infile = 'test_spmf.txt'
    base = 'Results'
    format = "spmf"
    delta = 0.0005
    start = 0.001
    threadlist = []
    for ratio in (start+mult*delta for mult in range(6,9)):
        options = {'threshold' : ratio, 'format': format}
        outfile = base + ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'gap' : 2000, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'gap' : 0, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'gap' : 1, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'gap' : 2, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'window' : 1, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'window' : 2, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'window' : 3, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'window' : 3, 'gap' : 0, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p)

        options = {'threshold' : ratio, 'window' : 3, 'gap' : 1, 'format': format}
        outfile = base+ ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
        p = Process(target=analyze, args=(infile,outfile,options))
        p.start()
        threadlist.append(p) 
    
        for thread in threadlist:
            thread.join()
"""


if __name__ == '__main__':
    
    path='./datasets'
    #infile = 'C01T5S250I003SP5_clean.txt'
    infile = '%s/C10T8S8I8-FF.txt' % (path)
    #infile = 'clean.txt'
    #infile = '%s/test_spmf.txt' % (path)
    #infile = '%s/test_ascii.txt' % (path)
    #path_res='%s/p6_Corpus.csv' %(path)
    #path_res='%s/p6_Corpus_reducido.csv' %(path)
    #infile = '%s/pei_ascii.txt' % (path)

    base = 'Results'
    delta = 0.0005
    start = 0.001
    ratio = start + 6 * delta
    #ratio = 4
    #formatfile = 'ascii'
    formatfile = 'spmf'

    # PrefixSpan
    options = {'threshold' : ratio, 'format': formatfile}
    outfile = base + ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
    analyze(infile,outfile,options)
    # # Copper
    # options = {'threshold' : ratio, 'minSseq': 1, 'maxSseq': 2, 'maxSize': 3, 'format': formatfile}
    # outfile = base + ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
    # analyze(infile,outfile,options)
    # WinGap
    # options = {'threshold' : ratio, 'window' : 3, 'gap' : 0, 'format': formatfile}
    # outfile = base + ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
    # analyze(infile,outfile,options)
    # I think this should be WinCop
    # options = {'threshold' : ratio, 'minSseq': 1, 'maxSseq': 2, 'maxSize': 3, 'window' : 3, 'gap' : 0, 'format': formatfile}
    # outfile = base + ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
    # analyze(infile,outfile,options)
    # WinCop
    # options = {'threshold' : ratio, 'minSseq': 1, 'maxSseq': 2, 'maxSize': 3, 'window' : 3, 'gap' : 0, 'logical': True, 'format': formatfile}
    # outfile = base + ''.join((str(opt[0])+str(options[opt]) for opt in options)) + '.txt'
    # analyze(infile,outfile,options)




    #u_db = open(infile, 'r')
    #for i in u_db:
    #    print(i)

    #s_db = fp.asciiFormater(u_db)
    #print(s_db)
    #options['threshold']=int(math.ceil(options['threshold']*len(s_db)))
    #res = ps.prefixspan(s_db, options)
    #out = open(outfile,'w')
    #out.write("Options: "+str(options)+'\n')
    #out.write("Patterns Found: " + str(len(res))+'\n')
    #out.write("Time Taken: " + str(end - start)+'\n')
    #for pat in sorted(res, key=lambda x: x[1]):
    #    out.write(str(pat)+'\n')
    #out.close()

    #infile = 'C01T5S250I003SP5.txt'
    #u_db = open(infile, 'r')
    #for i in u_db:
    #    print(i)
