Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
"""
Mutation Operators for Java code
implemented:
  LCR - logical connector replacement
  ABS - absolute value insertion
  UOI - unary operator insertion
  AOR - arithmetic operator replacement
  ROR - relatinal operator replacement
"""

def  AOR(filename, operators):
    """
    Orarithmetic Replacement mutation operator 
    Changes + to - and vice versa
    And changes * to / and vice versa
    """

    mutantsCount = 0

    if '+' in operators.keys() or '-' in operators.keys() or '/' in operators.keys() or '*' in operators.keys():
        with open(filename + '.java', 'r') as infile:
            content = infile.read()

    if '+' in operators.keys():
        for position in operators['+']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '-' + content[position + 1:] )
            mutantsCount += 1

    if '-' in operators.keys():
        for position in operators['-']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '+' + content[position + 1:] )
            mutantsCount += 1

    if '/' in operators.keys():
        for position in operators['/']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '*' + content[position + 1:] )
            mutantsCount += 1

    if '*' in operators.keys():
        for position in operators['/']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '/' + content[position + 1:] )
            mutantsCount += 1

    print('AOR mutation finished. Mutants generated: {0}'.format(mutantsCount))
