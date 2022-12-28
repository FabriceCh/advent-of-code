# face 1
def face1_left_trans(pos):
    return (49 - pos[0], 0)

def face1_right_trans(pos):
    return (pos[0], 0)

def face1_up_trans(pos):
    return (pos[1], 0)

def face1_down_trans(pos):
    return (0, pos[1])

# face 2
def face2_left_trans(pos):
    return (pos[0], 49)

def face2_right_trans(pos):
    return (49 - pos[0], 49)

def face2_up_trans(pos):
    return (49, pos[1])

def face2_down_trans(pos):
    return (pos[1], 49)

# face 3
def face3_left_trans(pos):
    return (0, pos[0])

def face3_right_trans(pos):
    return (49, pos[0])

def face3_up_trans(pos):
    return (49, pos[1])

def face3_down_trans(pos):
    return (0, pos[1])

# face 4
def face4_left_trans(pos):
    return (49 - pos[0], 0)

def face4_right_trans(pos):
    return (pos[0], 0)

def face4_up_trans(pos):
    return (pos[1], 0)

def face4_down_trans(pos):
    return (0, pos[1])

# face 5
def face5_left_trans(pos):
    return (pos[0], 49)

def face5_right_trans(pos):
    return (49 - pos[0], 49)

def face5_up_trans(pos):
    return (49, pos[1])

def face5_down_trans(pos):
    return (pos[1], 49)

# face 6
def face6_left_trans(pos):
    return (0, pos[0])

def face6_right_trans(pos):
    return (49, pos[0])

def face6_up_trans(pos):
    return (49, pos[1])

def face6_down_trans(pos):
    return (0, pos[1])
