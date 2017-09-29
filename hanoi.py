towers = []

def move(From,To):
    global towers
    if From == 'A':
        from_index = 0
    if From == 'B':
        from_index = 1
    if From == 'C':
        from_index = 2
    if To == 'A':
        to_index = 0
    if To == 'B':
        to_index = 1
    if To == 'C':
        to_index = 2
    towers[to_index].append(towers[from_index].pop())
    #print(towers)
    
def hanoi(n, a='A', b='B', c='C'):
    if n == 1:
        #print('move', a, '-->', c,' ')
        move(a,c)
        return
    hanoi(n-1, a, c, b)
    #print('move', a, '-->', c,' ')
    move(a,c)
    hanoi(n-1, b, a, c)
    
def hanoi_init(n):
    global towers
    tower = []
    for i in range(n):
        tower.append(i+1)
    towers = [list(reversed(tower)),[],[]]
    print(towers)
    hanoi(n)
    print(towers)
    


    
