import pandas as pd
from ast import literal_eval
import copper.dataprocessor as dp
import copper.fileprocessor as fp
import copper.prefixspan as ps
import time
import copper.profiling as pro

def test_file(support, time, memory, max_memory, results):
    # structure ==> support, time, memory, max memory, patterns
    # time in seconds
    # memory in MBs
    # max memory in MBs
    # patterns: quantity of patterns
    with open('results_copper_test.csv', 'a') as f:
        f.write(str(support)+','+str(time*1000)+','+str(memory/10**6)+','+str(max_memory/10**3)+','+str(len(results))+'\n')

if __name__ == "__main__":
    path = './datasets'
    path_res='%s/p6_Corpus_reducido.csv' % (path)

    threshold = 0.01

    data = pd.read_csv(path_res, sep=",", header=0, converters={"Corpus": literal_eval})
    sids = list(data["Clientes"])
    sequences = list(data["Corpus"])
    items_separated = True


    for i in range(100):
        print(threshold)
        options = {'threshold' : threshold, 'minSseq': 1, 'maxSseq': 5, 'minSize': 1, 'maxSize': 5}
        seq = dp.discretize_sequences(sequences, items_separated)

        u_db = fp.db_to_spmf(seq)
        s_db = fp.readDB(u_db, options)

        mem_before = pro.get_process_memory()
        mem_max_before = pro.get_max_resident_memory()
        time_start = time.time()
        result_mining = ps.prefixspan(s_db, options)
        time_end = time.time()
        mem_max_after = pro.get_max_resident_memory()
        mem_after = pro.get_process_memory()
        result_mining_undiscretize = dp.undiscretize_sequences(sequences, result_mining, items_separated)
        time_e = time_end - time_start
        memory_u = mem_after - mem_before
        memory_max = mem_max_after - mem_max_before

        test_file(threshold, time_e, memory_u, memory_max, result_mining_undiscretize)
        fp.get_result_file(result_mining_undiscretize, options, time_start, time_end, mem_after, mem_before, mem_max_after, mem_max_before)
        threshold += 0.01 
