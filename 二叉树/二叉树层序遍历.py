from collections import deque


def print_tree_layer(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        print(p.val)
        if p.lchild is not None:
            queue.append(p.lchild)
        if p.rchild is not None:
            queue.append(p.rchild)


def print_level(root, level):  # 调用多次

    #     for i in range(4):
    #         print_level(root,i)
    if root is None or level < 0:
        return 0
    elif level == 0:
        print(root.data)
        return 1
    else:
        return print_level(root.leftchild, level - 1), print_level(root.rightchild, level - 1)


def print_level_by_cow(proot):
    if not proot:
        return []
    resultlist = []
    curlayer = [proot]
    while curlayer:
        curlist = []
        nextlist = []
        for node in curlayer:
            curlist.append(node.val)
            if node.left:
                nextlist.append(node.left)
            if node.right:
                nextlist.append(node.right)
        resultlist.append(curlist)
        curlayer = nextlist
    return resultlist


def print_level_by_z(proot):
    resultarray = []
    if not proot:
        return resultarray
    curlayernode = [proot]
    isevenlayer = True
    while curlayernode:
        curlayervalue = []
        nextlayernode = []
        isevenlayer = not isevenlayer
        for node in curlayernode:
            curlayervalue.append(node.val)
            if node.left:
                nextlayernode.append(node.left)
            if node.right:
                nextlayernode.append(node.right)
        curlayernode = nextlayernode
        resultarray.append(curlayervalue[::-1]) if isevenlayer else resultarray.append(curlayervalue)
        return resultarray
