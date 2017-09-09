import random
answers = ['Yes',
           'Very probably',
           'Should not get your hopes up.',
           'No',
           'Eh, unlikely',
           'Would not bet on it.']

print('Think of a question and then press enter.')
input()
print(answers[random.randint(0, len(answers)-1)])
