def goalState(goal_state):
    current_state=4
    while current_state!=goal_state:
         if current_state<goal_state:
             current_state=current_state+1
         else:
             current_state=current_state-1
         print(current_state)
    print("goal state")
goalState(10)
