#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Profiling module
"""

import os
import psutil


def process_memory():
    """

    Parameters
    ----------

    Returns
    -------
    float
        get current memory of process

    """
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def max_resident_memory():
    """

    Parameters
    ----------

    Returns
    -------
    float
        get max memory of process

    """
    if psutil.LINUX or psutil.MACOS or \
       psutil.FREEBSD or psutil.NETBSD or \
       psutil.OPENBSD or psutil.BSD:
        import resource
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    elif psutil.WINDOWS:
        process = psutil.Process(os.getpid())
        return process.memory_info().peak_wset


def format_bytes(bytes):
    """
    [DEPRECATED]  format bytes in respective unit

    Parameters
    ----------
    bytes: float

    Returns
    -------
    string
        bytes depending quantity of bytes
    """
    if abs(bytes) < 1000:
        return str(bytes)+"B"
    elif abs(bytes) < 1e6:
        return str(round(bytes/1e3,2)) + "kB"
    elif abs(bytes) < 1e9:
        return str(round(bytes / 1e6, 2)) + "MB"
    else:
        return str(round(bytes / 1e9, 2)) + "GB"


def elapsed_since(start, end):
    """
    [DEPRECATED]  Elapsed time depending seconds

    Parameters
    ----------
    start: date
        start time
    end: date
        end time

    Returns
    -------
    string
        elapsed time in depending quantity of seconds elapsed
    """
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
    """

    Parameters
    ----------
    results: list

    Returns
    -------
    string
        number of patterns
    """
    return str(len(results)) + "Patterns" 
