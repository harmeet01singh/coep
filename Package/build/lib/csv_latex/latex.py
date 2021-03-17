def latex(expr):
    return f'${expr}$'

def superscript(variable, power):
    return f'{variable}^{{{power}}}'

def convert_to_term(coefficient, variable1, power1, variable2, power2):
    return (str(coefficient) if coefficient != 1 else '') + superscript(variable1, power1) + superscript(variable2, power2)

def to_frac(numerator, denominator):
    return f'$\\frac{{{numerator}}}{{{denominator}}}$'