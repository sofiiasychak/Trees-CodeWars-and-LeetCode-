def pre_order(node):
    """
    Pre-order traversal.
    """
    if node is None:
        return []

    result = []
    stack = [node]

    while stack:
        current = stack.pop()
        if current is None:
            continue

        result.append(current.data)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result

def in_order(node):
    """
    In-order traversal.
    """
    if node is None:
        return []

    result = []
    stack = []
    current = node

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.data)

        current = current.right

    return result

def post_order(node):
    """
    Post-order traversal.
    """
    if node is None:
        return []

    result = []
    stack1 = [node]
    stack2 = []

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    while stack2:
        result.append(stack2.pop().data)

    return result
