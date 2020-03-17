#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import psutil
import resource

def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def get_max_resident_memory():
    #if platform.system() == 'Linux':
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    #elif platform.system() == 'Windows':
    #    return process.memory_info().peak_wset

def format_bytes(bytes):
    if abs(bytes) < 1000:
        return str(bytes)+"B"
    elif abs(bytes) < 1e6:
        return str(round(bytes/1e3,2)) + "kB"
    elif abs(bytes) < 1e9:
        return str(round(bytes / 1e6, 2)) + "MB"
    else:
        return str(round(bytes / 1e9, 2)) + "GB"


def elapsed_since(start, end):
    #return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))
    elapsed = end - start
    if elapsed < 1:
        return str(round(elapsed*1000,2)) + "ms"
    if elapsed < 60:
        return str(round(elapsed, 2)) + "s"
    if elapsed < 3600:
        return str(round(elapsed/60, 2)) + "min"
    else:
        return str(round(elapsed / 3600, 2)) + "hrs"


def number_patterns(results):
    return str(len(results)) + "Patterns" 
