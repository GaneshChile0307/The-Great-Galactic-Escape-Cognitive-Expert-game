import random

'''
Calculate distance of each tile from each sub-goal. This information will be globally available for agent in order to make decisions
'''
def calc_dist3():
    dist_goal3=[['L1', 3],['L2', 2],['L3', 1],['L4', 0],['L5', 4],['L6', 3],['L7', 2],['L8', 1],['L9', 5],['L10', 4],['L11', 3],['L12', 2],['L13', 6],['L14', 5],['L15', 4],['L16', 3]]
    return dist_goal3

def calc_dist1():
    dist_goal1 = [['L1',3],['L2',2],['L3',3],['L4',4],['L5',2],['L6',1],['L7',2],['L8',3],['L9',1],['L10',0],['L11',1],['L12',2],['L13',2],['L14',1],['L15',2],['L16',3]]
    return dist_goal1

def calc_dist2():
    dist_goal2 = [['L1',6],['L2',5],['L3',4],['L4',3],['L5',5],['L6',4],['L7',3],['L8',2],['L9',4],['L10',3],['L11',2],['L12',1],['L13',3],['L14',2],['L15',1],['L16',0]]
    return dist_goal2



def make_landscape1(landscape1):
    landscape1 = [
    ['L1', ['C1', 'open', 1.0], 'L2'],
    ['L1', ['C2', 'open', 1.0], 'L5'],

    ['L2', ['C3', 'open', 1.0], 'L6'],
    ['L2', ['C3', 'open', 1.0], 'L3'],
    ['L2', ['C4', 'open', 1.0], 'L1'],

    ['L3', ['C3', 'open', 1.0], 'L2'],
    ['L3', ['C3', 'open', 1.0], 'L7'],
    ['L3', ['C4', 'open', 1.0], 'L4'],

    ['L4', ['C1', 'open', 1.0], 'L8'],
    ['L4', ['C2', 'open', 1.0], 'L3'],

    ['L5', ['C3', 'open', 1.0], 'L1'],
    ['L5', ['C3', 'open', 1.0], 'L6'],
    ['L5', ['C4', 'open', 1.0], 'L9'],

    ['L6', ['C3', 'open', 1.0], 'L2'],
    ['L6', ['C3', 'open', 1.0], 'L7'],
    ['L6', ['C4', 'open', 1.0], 'L5'],
    ['L6', ['C4', 'open', 1.0], 'L10'],

    ['L7', ['C3', 'open', 1.0], 'L3'],
    ['L7', ['C3', 'open', 1.0], 'L6'],
    ['L7', ['C4', 'open', 1.0], 'L8'],
    ['L7', ['C4', 'open', 1.0], 'L11'],

    ['L8', ['C3', 'open', 1.0], 'L4'],
    ['L8', ['C3', 'open', 1.0], 'L7'],
    ['L8', ['C4', 'open', 1.0], 'L12'],

    ['L9', ['C3', 'open', 1.0], 'L5'],
    ['L9', ['C3', 'open', 1.0], 'L10'],
    ['L9', ['C4', 'open', 1.0], 'L13'],

    ['L10', ['C3', 'open', 1.0], 'L6'],
    ['L10', ['C3', 'open', 1.0], 'L9'],
    ['L10', ['C4', 'open', 1.0], 'L11'],
    ['L10', ['C4', 'open', 1.0], 'L14'],

    ['L11', ['C3', 'open', 1.0], 'L7'],
    ['L11', ['C3', 'open', 1.0], 'L10'],
    ['L11', ['C4', 'open', 1.0], 'L12'],
    ['L11', ['C4', 'open', 1.0], 'L15'],

    ['L12', ['C3', 'open', 1.0], 'L8'],
    ['L12', ['C3', 'open', 1.0], 'L11'],
    ['L12', ['C4', 'open', 1.0], 'L16'],

    ['L13', ['C3', 'open', 1.0], 'L14'],
    ['L13', ['C3', 'open', 1.0], 'L9'],

    ['L14', ['C3', 'open', 1.0], 'L10'],
    ['L14', ['C3', 'open', 1.0], 'L13'],
    ['L14', ['C4', 'open', 1.0], 'L15'],

    ['L15', ['C3', 'open', 1.0], 'L11'],
    ['L15', ['C3', 'open', 1.0], 'L14'],
    ['L15', ['C4', 'open', 1.0], 'L16'],

    ['L16', ['C3', 'open', 1.0], 'L12'],
    ['L16', ['C3', 'open', 1.0], 'L15']]

    return landscape1

'''
Working memory and its components, Next Goal Locatons, and Long term memory - global variables
'''

WM = [['GoalLoc', 'X'],
      ['StartLoc', 'Y'],
      ['LastLoc', 'NA'],
      ['LastAction', []],
      ['CurrentLoc', 'Z'],
      ['CurrentOptions', []],
      ['NextGoalLoc', 'N'],
      ['DistToGoal', 99],
      ['PrevDistToGoal', 99]
      ]

NGL = ['L10',
       'L16',
       'L4',]

LTM = [[]]


def initial_WM(start, goal):
    WM.remove(WM[0])
    WM.insert(0, ['GoalLoc', goal])
    WM.remove(WM[1])
    WM.insert(1, ['StartLoc', start])
    WM.remove(WM[4])
    WM.insert(4, ['CurrentLoc', start])
    WM.remove(WM[6])
    WM.insert(6, ['NextGoalLoc', NGL[0]])
    WM.remove(WM[7])
    WM.insert(7, ['DistToGoal', 3])
    WM.remove(WM[8])
    WM.insert(8, ['PrevDistToGoal', 99])
    print("\n", "Next Goal: ", WM[6])
    print("Initial path memory", LTM[0])
    return WM

'''
CHeck current options available for the agent from current location. this returns available options from current environment
'''
def see_affordances(landscape, current_location):
    action_list = []
    for item in landscape:
        if item[0] == current_location:
            action_list = action_list + [item]
    encode_options_WM(action_list)
    return action_list

'''
Insert current options available for the agent into the working memory. This is like perception - where agent can see 
its options and hence they go in the working memory
'''
def encode_options_WM(action_list):
    WM.remove(WM[5])
    WM.insert(5, ['CurrentOptions', action_list])
    return WM

'''
Upon selecting an action from available options, that action is executed and all the components of WM are updated here
'''
def execute_action(action, nglcounter):
    updateLastLoc(action)
    updateLastAction(action)
    updateCurrentLoc(action)
    resetCurrentOptions()
    encodeintoLTM(action)
    updatePathLTM(action)
    nglcounter = updateNextGoal(nglcounter)
    updatedistances(action)
    return nglcounter


def updateLastLoc(action):
    WM.remove(WM[2])
    WM.insert(2, ['LastLoc', action[0]])
    return WM


def updateLastAction(action):
    WM.remove(WM[3])
    WM.insert(3, ['LastAction', action])
    return WM


def updateCurrentLoc(action):
    WM.remove(WM[4])
    WM.insert(4, ['CurrentLoc', action[-1]])
    #print("\n", "Updating CurrentLoc to", WM[4], "\n")
    return WM

def updatedistances(action):
    if WM[6][1] == 'L10':
        for item in dist_goal1:
            if item[0] == WM[4][1]:
                WM[8][1] = WM[7][1]
                WM[7][1]=item[1]

    if WM[6][1] == 'L16':
        for item in dist_goal2:
            if item[0] == WM[4][1]:
                WM[8][1] = WM[7][1]
                WM[7][1]=item[1]
    if WM[6][1] == 'L4':
        for item in dist_goal3:
            if item[0] == WM[4][1]:
                WM[8][1] = WM[7][1]
                WM[7][1]=item[1]

def resetCurrentOptions():
    WM.remove(WM[5])
    WM.insert(5, ['CurrentOptions', []])
    return WM


def encodeintoLTM(action):
    LTM.insert(1, action)
    return LTM


def updatePathLTM(action):
    #print("\n", "Executing action", action)
    path_memory = LTM[0]
    LTM.remove(LTM[0])
    LTM.insert(0, path_memory + [action[-1]])
    # print("\n", "Updated path memory", LTM[0])
    return LTM

def updateNextGoal(nglcounter):
    if WM[4][1] == WM[6][1] and WM[6][1] != 'L4':
        nglcounter = nglcounter + 1
        WM.remove(WM[6])
        WM.insert(6, ['NextGoalLoc', NGL[nglcounter]])
        WM.remove(WM[8])
        WM.insert(8, ['PrevDistToGoal', 99])
        WM.remove(WM[7])
        WM.insert(7, ['DistToGoal', 99])
        print("\n", "Updated Next Goal to: ", WM[6])
        print("Updated path memory", LTM[0])

    return nglcounter

'''
THe executive function for Random approacjh without any strategy and without any learning. This is just for reference, 
if you want to execute the random approach, just change the execution function in the mainfunction
'''
def ExecutiveFunction(maxcycles):
    initial_WM('L1', 'L4')
    step_counter = 0
    nglcounter = 0
    while maxcycles > step_counter:
        GoalLoc = WM[0][1]
        CurrentLoc = WM[4][1]
        if CurrentLoc == GoalLoc and WM[6][1] == GoalLoc:
            print("Arrived at location", GoalLoc)
            print("Total steps: ", step_counter)
            return step_counter
        else:
            options = see_affordances(environment1, CurrentLoc)
            options = prune_options2(options)
            print("\n", "options are", options)
            if options == []:
                print("Run out of actions to try in", CurrentLoc)
                return CurrentLoc, step_counter
            else:
                current_action = select_action(options)
                print("\n", "action selected", current_action)
                nglcounter = execute_action(current_action,nglcounter)
                step_counter = step_counter + 1
    print("Maximum no of cycles reached", CurrentLoc)
    print("Total steps: ", step_counter)
    '''print("--- LTM len - ", len(LTM))'''
    return CurrentLoc, step_counter


'''
Here is the executive function of our agent. This funsion is used for learning from previous mistakes and prune unnecessary and ineffective options.
by pruning options according to the distance from next goal, the agent learns its path over time. Please read model description for more details.
'''

def ExecutiveFunctionNew(maxcycles):
    initial_WM('L1', 'L4')
    step_counter = 0
    nglcounter = 0
    result = 0
    while maxcycles > step_counter:
        GoalLoc = WM[0][1]
        CurrentLoc = WM[4][1]
        if CurrentLoc == 'L14':
            result = 1
            learndanger()
            return [result, step_counter]
        if CurrentLoc == GoalLoc and WM[6][1] == GoalLoc:
            print("\n\n\t\tMission Complete! Arrived at EARTH and Agent Won Full Prize in %d steps" % step_counter)
            print("")
            return [result, step_counter]
        else:
            if WM[7][1] <= WM[8][1]:
                if WM[6][1] == 'L10':
                    options = see_affordances(environment1, CurrentLoc)
                if WM[6][1] == 'L16':
                    options = see_affordances(environment2, CurrentLoc)
                if WM[6][1] == 'L4':
                    options = see_affordances(environment3, CurrentLoc)
                options = prune_options2(options)
                #print("\n", "options are", options)
                if options == []:
                    print("Run out of actions to try in", CurrentLoc)
                    return CurrentLoc, step_counter
                else:
                    current_action = select_action(options)
                    #print("\n", "action selected", current_action)
                    nglcounter = execute_action(current_action,nglcounter)
                    step_counter = step_counter + 1
            else:
                if WM[6][1] == 'L10':
                    options = see_affordances(environment1, CurrentLoc)
                if WM[6][1] == 'L16':
                    options = see_affordances(environment2, CurrentLoc)
                if WM[6][1] == 'L4':
                    options = see_affordances(environment3, CurrentLoc)
                options = learnpath(options)
                # print("\n", "Wrong Path! Backtracking using - ", options)
                if options == []:
                    print("Run out of actions to try in", CurrentLoc)
                    return CurrentLoc, step_counter
                else:
                    current_action = select_action(options)
                    #print("\n", "action selected", current_action)
                    nglcounter = execute_action(current_action, nglcounter)
                    step_counter = step_counter + 1
                    if WM[6][1] == 'L10':
                        updateoptions(environment1)
                    if WM[6][1] == 'L16':
                        updateoptions(environment2)
                    if WM[6][1] == 'L4':
                        updateoptions(environment3)
    print("Maximum no of cycles reached", CurrentLoc)
    print("Total steps: ", step_counter)
    return [result, step_counter]


def learnpath(options):
    action_list = []
    for item in options:
        if item[-1] == WM[2][1]:
            action_list = action_list + [item]
    encode_options_WM(action_list)
    return action_list

'''If agent dies at the danger (L14), all the links to this tile are removed. therefore agent will not go into the danger again '''
def learndanger():
    for item in environment1:
        if item[-1] == 'L14':
            environment1.remove(item)
    for item in environment2:
        if item[-1] == 'L14':
            environment2.remove(item)
    for item in environment3:
        if item[-1] == 'L14':
            environment3.remove(item)

def updateoptions(environment):
    for item in environment:
        if item[0] == WM[4][1] and item[-1] == WM[2][1]:
            environment.remove(item)
    return environment

def prune_options(options):
    newlist = []
    for item in options:
        if item not in LTM:
            newlist = newlist + [item]
    return newlist


def prune_options2(options):
    return options

'''Randomly select action from current available options'''
def select_action(options):
    selected_action = random.choice(options)
    return selected_action

def mainfuncion():
    print("\n", "--------------------- Welcome to The Great Galactic Adventure -------------------")
    print("\n\n Agent Ready!! ")
    print("\n", "-------------- RUN 1 -----------------")
    result = ExecutiveFunctionNew(40)
    if result[0] == 1:
        print("\n\t\t Agent Killed By The Alien Spaceship!! GAME OVER !!!\n", WM[3][1])
    print("\t In this run, Agent Travelled : ", LTM[0][-result[1]:])
    print("\n", "-------------- RUN 2 -----------------")
    result = ExecutiveFunctionNew(40)
    if result[0] == 1:
        print("\n\t\t Agent Killed By The Alien Spaceship!! GAME OVER !!!\n", WM[3][1])
    print("\t In this run, Agent Travelled : ", LTM[0][-result[1]:])
    print("\n", "-------------- RUN 3 -----------------")
    result = ExecutiveFunctionNew(40)
    if result[0] == 1:
        print("\n\t\t Agent Killed By The Alien Spaceship!! GAME OVER !!!\n", WM[3][1])
    print("\t In this run, Agent Travelled : ", LTM[0][-result[1]:])
    print("\n", "-------------- Final Run -----------------")
    result = ExecutiveFunctionNew(40)
    if result[0] == 1:
        print("\n\t\t Agent Killed By The Alien Spaceship!! GAME OVER !!!\n Please Start Over!!!", WM[3][1])
    print("\t In this run, Agent Travelled : ", LTM[0][-result[1]:])


'''
Create Pathways to reach each sub-goal. When agent is trying to reach for particular subgoal, that specific envisonment is used for 
selecting available options. We are keeping the separate environments for separate subgoals so that path modifications done for one 
subgoals should not affect options for any other subgoals.
'''
environment1 = make_landscape1('landscape1')
environment2 = make_landscape1('landscape1')
environment3 = make_landscape1('landscape1')
dist_goal1 = calc_dist1()
dist_goal2 = calc_dist2()
dist_goal3 = calc_dist3()

'''
Main function - program starts here
'''
mainfuncion()