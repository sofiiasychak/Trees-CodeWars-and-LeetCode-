def tree_by_levels(node):
    '''Sorting binary tree by levels'''
    if node is None:
        return []

    result = []
    queue = [node]

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return result
