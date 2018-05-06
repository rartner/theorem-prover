from copy import deepcopy
from node import Node

branches = 0

def compute(formulas):
    global branches
    for f in formulas:
        print (f)
    print ('\n-------')
    expand_alpha(formulas)
    if (closed(formulas)):
        branches += 1
        return True, branches
    beta = get_last_beta(formulas)
    if (beta == None):
        branches += 1
        if (not closed(formulas)):
            return get_valuation(formulas), branches
        return True, branches
    else:
        c1, c2 = beta.expand()
        f1, f2 = deepcopy(formulas), deepcopy(formulas)
        f1.append(c1)
        f2.append(c2)
        b1, _ = compute(deepcopy(f1))
        if (b1 != True):
            return b1, branches
        b2, _ = compute(deepcopy(f2))
        if (b2 != True):
            return b2, branches
        else:
            return True, branches

def expand_alpha(formulas):
    for formula in formulas:
        if (formula.is_alpha() and not formula.is_atom() and not formula.expanded):
            c1, c2 = formula.expand()
            formulas.append(c1)
            if (c2 != None): formulas.append(c2)

def get_last_beta(formulas):
    for formula in list(reversed(formulas)):
        if (not formula.is_alpha() and formula.expanded == False and not formula.is_atom()):
            return formula
    return None

def closed(formulas):
    last_atom = formulas[len(formulas)-1]
    if (has_absurd(last_atom, formulas)):
        return True
    else:
        return False

def has_absurd(atom, formulas):
    for i in range(len(formulas) - 1):
        formula = formulas[i]
        if (formula.is_atom() and not formula.expanded):
            if (atom.token == formula.token):
                if (atom.valuation != formula.valuation):
                    return True
    return False

def get_valuation(formulas):
    valuation = []
    for f in formulas:
        if (f.is_atom()):
            valuation.append('{}: {}'.format(f.token, f.valuation))
    return valuation
