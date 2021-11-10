import random

def is_float(string, parameters_dictionary):
    try:        
        return float(string)
    except ValueError:
        try:
            return parameters_dictionary.get(string)
        except ValueError:
            return string

def Parametric_string_to_list(sequence, parameters_dictionary):
    out = []
    parameters = []
    aux = ''
    filling_parameters = False
    for character in sequence:
        if character == '(':
            filling_parameters = True
        elif character == ')':
            filling_parameters = False
            if aux != '':
                parameters.append(is_float(aux, parameters_dictionary))
                aux = ''
            out[-1].append(parameters)
            parameters = []
            
        elif not filling_parameters:
            out.append([character])
            
        elif character != ',':
            aux = ''.join([aux, character])
        elif character == ',':
            parameters.append(is_float(aux, parameters_dictionary))
            aux = ''
            
    return out
            
def Transform_multiple(sequence, transformations, iterations):
    for _ in range(iterations):
        sequence = Transform_sequence(sequence, transformations)
    return sequence

    
def Transform_sequence(sequence, transformations):
    return ''.join(random.choice(transformations.get(c, c)) for c in sequence)