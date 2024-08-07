################ Project: Escaping The Maze (Reeborg's World) ################
# Note: Earlier version of this code had a potential infinite loop in 2 places. 
#       I checked to see if the last move repeating and corrected it.

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def is_repeating(move_set, count):
#     i = -1
#     repeat = 1
#     while i > 0 - len(move_set) and move_set[i] == move_set[i - 1]:
#         i -= 1
#         repeat += 1
#     if repeat >= count:
#         return True
#     else:
#         return False

# move_set = []
    
# while not at_goal():
#     if len(move_set) >= 4 and is_repeating(move_set, 4):
#         turn_left()
#         move_set.append(turn_left)
#     if right_is_clear():
#         turn_right()
#         move()
#         move_set.append("turn_rightmove")
#     elif front_is_clear():
#         move()
#         move_set.append("move")
#     else:
#         turn_left()
#         move_set.append("turn_left")
