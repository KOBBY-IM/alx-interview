#!/usr/bin/python3
"""A module containing the function canUnlockAll"""


def canUnlockAll(boxes):
    """A function to check if all locked boxes can be unlocked
    """

    # Create a set to keep track of the unlocked boxes
    unlocked_boxes = set([0])
    
    # Create a list to store the keys
    keys = boxes[0]
    
    # Iterate through the keys and unlock the corresponding boxes
    while keys:
        key = keys.pop(0)
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.extend(boxes[key])
    
    # Check if all boxes are unlocked
    return len(unlocked_boxes) == len(boxes)