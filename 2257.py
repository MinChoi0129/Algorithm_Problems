MassTable = {'H' : 1, 'C' : 12, 'O' : 16}
OtherTable = ['2', '3', '4', '5', '6', '7', '8', '9', '(', ')']
chemicalStatement = input()


def chemicalMassCalculator(statement): # H20 LEN = 3
    chemicalMass = 0
    i = 0
    while i != len(statement):
        try:
            if statement[i] == '(':
                tmpChemicalStatement = ""
                while True:
                    i += 1
                    if statement[i] == ')':
                        i += 1
                        break
                    else:
                        tmpChemicalStatement += statement[i]
                
                multiplier = 1
                try:
                    if statement[i] in OtherTable[:8]:
                        multiplier = int(statement[i])
                except:
                    pass
                
                chemicalMass += (multiplier * chemicalMassCalculator(tmpChemicalStatement))
                
            elif statement[i] not in OtherTable:
                if statement[i+1] in OtherTable[:8]:
                    chemicalMass += (MassTable[statement[i]] * int(statement[i+1]))
                    i += 2
                else:
                    chemicalMass += MassTable[statement[i]]
                    i += 1
            else:
                i += 1
            
        except:
            chemicalMass += MassTable[statement[-1]]
            i += 1
            
    return chemicalMass
                    
print(chemicalMassCalculator(chemicalStatement))