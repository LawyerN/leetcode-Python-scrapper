def simplify_path(path):
    # Split path into a list of directory names
    dirs = path.split(\'/\')
    # Initialize the stack of directories
    stack = []
    # Iterate through the directories
    for d in dirs:
        # Ignore double slashes
        if d == \'\':
            continue
        # If it\'s a double period, pop the top directory from the stack
        elif d == \'..\':
            if stack:
                stack.pop()
        # If it\'s a single period or a regular directory name, add it to the stack
        elif d != \'.\':
            stack.append(d)
    # Construct the simplified canonical path
    simplified_path = \'/\' + \'/\'.join(stack)
    return simplified_path