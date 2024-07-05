#!/usr/bin/python3
'''Module for handling lockboxes.
'''


def canUnlockAll(boxes):
    '''Determines if all boxes in a list of boxes containing keys
    (indices) to other boxes can be unlocked, starting with the first
    box being unlocked.
    '''
    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0]).difference(unlocked)
    while keys:
        key = keys.pop()
        if key < 0 or key >= n:
            continue
        if key not in unlocked:
            keys.update(boxes[key])
            unlocked.add(key)
    return len(unlocked) == n
