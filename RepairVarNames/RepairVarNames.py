def pep8(func):
    def repairVarName(*args, **kwargs): # Vars func is defined in lower_case_with_underscores and we activate it with camel case
        newKwargs = {}
        for varName, value in kwargs.items():  # Move on every var name (key) in kwargs
            firstChar = 1
            newVarName = ""
            for charInWord in varName[:]: # Add under score
                if firstChar == 1: # First char in name
                    firstChar = 0
                    newVarName += charInWord.lower() # Change to lower and add
                elif charInWord.isupper(): # Start of new word
                    newVarName += "_"  # Add under score before char
                    newVarName += charInWord.lower()  # Change to lower and add
                else: # Not first char and not under score
                    newVarName += charInWord
            newKwargs[newVarName] = kwargs[varName]
        return func(*args, **newKwargs)
    return repairVarName

# Checks for pep8
@pep8
def f(x, foo_bar, stam, yet_another_silly_name):
    return x * 1000 + foo_bar * 100 + stam * 10 + yet_another_silly_name
assert (f(1, YetAnotherSillyName=2, stam=9, fooBar=4) == 1492)