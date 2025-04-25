from git import Git
from os.path import exists, isdir
from os import listdir

deductions = []

def DFS(path, depth = 0, max_depth = 4):  # prints directories under path
    if depth > max_depth:
        return
    for entry in listdir(path):
        entry_path = path + '/' + entry
        print(' ' * depth + entry)
        if ('__pycache__' not in entry_path) and ('.git' not in entry_path) and isdir(entry_path):
            DFS(entry_path, depth + 1, max_depth)

def deduct(answer=None, points=2, reason=''):
    if answer is None or not answer:
        deductions.append((points, reason))
            

LOCAL = './repos/'
FEEDBACK = './feedback/'
REMOTE = input('>>> Remote?  ')

Git(LOCAL).clone(REMOTE)
name = REMOTE[:REMOTE.find('2025') + len('2025')]
name = name[name.rfind('/') + len('/'):]

if (input(f'>>> `{name}` okay?  ') != 'y'):
    deduct(None, 2, f'Repo. name <{name}> not standard.')
    name = input('>>> Name?  ')

#checks = [
#    LOCAL + name + '/data',
#   LOCAL + name + '/src',
#    LOCAL + name + '/README.md',
#   LOCAL + name + '/deliverables',
#   LOCAL + name + '/deliverables/presentation/final.pdf',
#   LOCAL + name + '/deliverables/presentation/midterm.pdf',
 #   LOCAL + name + '/deliverables/final_idea.pdf',
  #  LOCAL + name + '/deliverables/three_ideas.pdf'
#]

#for item in checks:
 #   deduct(exists(item), 2, f'<{item}> does not exist.')
  #  if not exists(item):
   #     print(f'<{item}> does not exist.')

print('\n *** Presentation ***\n')
deduct(
    input('>>> Presentation quality?  ') == 'y',
    2,
    'Presentation poorly done (too many words/slides, blurry figures, poor organisation etc.)'
)
deduct(
    input('>>> Presentation meets requirments?  ') == 'y',
    5,
    'Presentation does not meet requirments.'
)

#if (not exists(checks[0])):
 #   temp = input('>>> Data dir name?  ')
  #  checks[0] = temp if temp == '?' else LOCAL + name + temp

#print('\n *** Data Directory ***\n')
#if checks[0] != '?':
 #   DFS(checks[0])
#print('\n')

deduct(
    input('>>> Can they find the file?  ') == 'y',
    5,
    'They could not find their main data file.'
)
deduct(
    input('>>> Can they show where it is read?  ') == 'y',
    5,
    'They could not show the line number where data is being read.'
)



print('\n *** Source Directory ***\n')
#if (not exists(checks[1])):
 #   checks[1] = LOCAL + name + input('>>> Source dir name?  ')
#DFS(checks[1])
#print('\n')

deduct(
    input('>>> Does not have extra files?  ') == 'y',
    2,
    'They have extra cluter files/or files they can\'t explain.'
)
deduct(
    input('>>> Can they maintain their code?  ') == 'y',
    5,
    'They are not familiar with their source code.'
)

print('\n *** Viva ***\n')
deduct(
    input('>>> Can they do basic data manipulation?  ') == 'y',
    5,
    'They can not write code at a masters level.'
)

total = 100
report = f'Deductions for {name}:\n\n'
for p, reason in deductions:
    report += f'{-1*p:5d}   {reason}\n'
    total -= p

report += f'\nTotal: {total}/100'

print(report)
with open(F'{FEEDBACK}/{name}.feedback', 'w') as fl:
    fl.write(report)
