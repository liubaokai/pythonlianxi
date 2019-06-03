class btree():
    def __init__(self):
        self.data = None
        self.leftchild = None
        self.rightchild = None

def array_to_btree(arr,start,end):
    root = None
    if end >= start:
        root = btree()
        mid = (start + end + 1) // 2
        root.data = arr[mid]
        root.leftchild = array_to_btree(arr, start, mid-1)
        root.rightchild = array_to_btree(arr, mid+1, end)
    else:
        root = None
    return root

def print_btree_midorder(root):
    if root is None:
        return
    if root.leftchild is not None:
        print_btree_midorder(root.leftchild)
    print(root.data)
    if root.rightchild is not None:
       print_btree_midorder(root.rightchild)

def print_level(root,level):
    if root is None or level < 0:
        return 0
    elif level == 0:
        print(root.data)
        return 1
    else:

        return print_level(root.leftchild, level-1), print_level(root.rightchild, level-1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = array_to_btree(arr, 0, len(arr) - 1)
    # print_btree_midorder(root)
    for i in range(4):
        print_level(root,i)