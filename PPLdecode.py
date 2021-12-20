import random
import re
import copy

def Get_value(string):
    try:        
        return eval(string)
    except:
        return string

def Try_dictionary(dictionary, key):
    try:
        return dictionary[key]
    except:
        return key

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

def Deparametrize(sequence, parametric_dictionary):
    for i in sequence:
        for j in i[1]:            
            separated = re.split('(\W)',j)
            deparametrize = ''.join([str(Try_dictionary(parametric_dictionary, k)) for k in separated])
            values = Get_value(deparametrize)
            i[1] = values

def Parametric_string_to_list(sequence):
    # First, ignore spaces and split into list based on '-->'
    sequence = sequence.replace(' ', '')
    sequence_list = sequence.split('-->')
            
    out = []
    aux_list = []
    parameters = []
    aux = ''
    opened_parenthesis = 0
    for sentence in sequence_list:
        for character in sentence:
            if character == ')':
                opened_parenthesis -= 1
                
            if opened_parenthesis == 0:
                if character == ')':
                    if aux != '':
                        parameters.append(aux)
                        aux = ''
                    aux_list[-1].append(parameters)
                    parameters = []
                elif character != '(':
                    aux_list.append([character])
                                
            elif opened_parenthesis > 0:
                if character == ',' and opened_parenthesis == 1:
                    parameters.append(aux)
                    aux = ''
                else:
                    aux = ''.join([aux, character])
            
            if character == '(':
                opened_parenthesis += 1
        out.append(aux_list)
        aux_list = []
        
    for l in out:
        for p in l:
            if len(p) == 1:
                p.append([''])
    
    if len(out) == 1:
        out = out[0]
    return out
            
def Transform_parametric(sequence, transformation):
    out = []
    for s in sequence:
        if s[0] == transformation[0][0][0]:
            aux_transform = copy.deepcopy(transformation[1])
            for k in range(len(aux_transform)):
                for i in range(len(aux_transform[k][1])):
                    for j in range(len(transformation[0][0][1])):
                        for l in range(len(s[1])):
                            aux_transform[k][1][i] = aux_transform[k][1][i].replace(transformation[0][0][1][j], s[1][l])
            out.extend(aux_transform)
        else:
            out.append(s)
    
    return out

def Transform_multiple(sequence, transformations, iterations):
    for _ in range(iterations):
        sequence = Transform_parametric(sequence, transformations)
    return sequence

    
def Transform_sequence(sequence, transformations):
    return ''.join(random.choice(transformations.get(c, c)) for c in sequence)