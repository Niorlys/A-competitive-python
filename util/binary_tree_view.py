from math import log2

def get_levels(arr, nodes=None):
    if not nodes:
        levels = [[arr[0]]]
        levels.extend(get_levels(arr, nodes=(1,2)))
        return levels
    
    levels = [[arr[index] for index in nodes]]
    new_nodes = []
    for index in nodes:
        left_child = 2 * index + 1
        if left_child < len(arr):
            new_nodes.append(left_child)
        else:
            levels.extend(get_levels(arr, nodes=new_nodes) if new_nodes else [])
            return levels
        if left_child + 1 < len(arr):
            new_nodes.append(left_child+1)
        else:
            levels.extend(get_levels(arr, nodes=new_nodes))
            return levels
    levels.extend(get_levels(arr, nodes=new_nodes))
    return levels

def craft_tree(arr, h):
    levels = get_levels(arr)
    branch_size = 1
    #Base
    pieces = ["   ".join(map(str, levels.pop()))]
    base_length = len(pieces[-1])
    diff = 1
    while branch_size <= h:
        for _ in range(diff):
            piece = []
            space = True
            status = '/'
            for i in range(base_length):
                if status == '/' and pieces[-1][i]==" ":
                    if space and pieces[-1][i - 1]!=" ":
                        piece.append("/")
                        status='\\'
                    else:
                        piece.append(" ")
                        space = True
                elif i+1 < base_length and pieces[-1][i]==" ":
                    if pieces[-1][i + 1]!=" ":
                        piece.append("\\")
                        status = '/'
                        space = False
                    else:
                        piece.append(" ")
                else:
                    piece.append(" ")
            pieces.append("".join(piece))
        
        level_index = 0
        current_level = levels.pop()
        if len(current_level) == 1:
            pieces.append(str(current_level[0]).center(base_length))
            return pieces
        piece = []
        node_indexes = []
        for i in range(0,base_length):
            if  i - 1 > 0 and pieces[-1][i-1] == '/':
                piece.append(str(current_level[level_index]))
                level_index+=1
                node_indexes.append(i)
            else:
                piece.append(" ")
        pieces.append("".join(piece))
        diff = (node_indexes[-1]-node_indexes[-2] - 1)//2
        branch_size+=1 
    return pieces

def print_tree(arr):
    arr = arr[:]
    if len(arr) > 15:
        raise ValueError("This works well only for arrays with length less than 16")
    h = int(log2(len(arr)))
    p = 2**(h+1)
    if len(arr) != p-1:
        arr.extend(["*" for _ in range(1,p-len(arr))])
    pieces = craft_tree(arr, h)
    for i in range(1, len(pieces) + 1):
        print(pieces[-i])         
        
if __name__ == '__main__':
    arr = list(range(1,16))
    print_tree(arr)
