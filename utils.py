def clean_return_carriage(file):
    output = open('clean.txt', 'wt')
    input = open(file,'rt')
    lines = iter(input.readlines())
    input.close()
    while True:
        try:
            line = next(lines)
            for i in range(len(line)):
                if(line[i] == '\r'):
                    print('retorno')
            output.write(line)
        except StopIteration:
            break
    output.close()
    
