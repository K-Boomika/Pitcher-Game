import sys
from collections import deque

class TreeNode:
    def __init__(self, state, inf, stopstate, heuristic, cost):
        self.state = state
        self.inf = inf
        self.stopstate = stopstate
        self.heuristic = heuristic
        self.cost = cost
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root
        self.leaf_nodes = []
        self._build_leaf_nodes_list()

    def add_node(self, parent, child):
        parent.children.append(child)
        self._build_leaf_nodes_list()

    def update_node_stopState(self, node, new_value):
        node.stopstate = new_value
        self._build_leaf_nodes_list()

    def _build_leaf_nodes_list(self):
        self.leaf_nodes = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if not node.children:
                if node.stopstate != 1:
                    self.leaf_nodes.append(node)
            else:
                for child in node.children:
                    stack.append(child)

    def print_level_wise(self):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.state," ",node.inf," ",node.stopstate, end='\n')
            for child in node.children:
                queue.append(child)
        print()

def getData(filename):
    file = open(filename,"r+")
    str = file.read()
    str = str.strip()
    data = str.split('\n')
    pitchers = list(map(int, data[0].split(',')))
    target = int(data[1])
    file.close()
    return [pitchers, target]

def heuristics(state, inf, target):
    if inf==target:
        return 0
    else:
        return abs(sum(state)+inf-target)

def endConditionNotReached(tree):
    min_cost = min((x.cost + x.heuristic for x in tree.leaf_nodes if x.stopstate == 0 or x.stopstate == 2), default=float('inf'))
    for node in tree.leaf_nodes:
        if node.stopstate == 0 and node.cost + node.heuristic <= min_cost:
            return True
        elif node.stopstate == 0 and node.cost > min_cost:
            tree.update_node_stopState(node,1)
    return False

def possibleCombinations(node, statesVal, capacity, target):
    possibleStates = []
    # Fill pitcher with water
    for idx, pitcher in enumerate(node.state):
        if pitcher < capacity[idx]:
            temp = node.state.copy()
            temp[idx] = capacity[idx]
            state = [temp, node.inf]
            if state not in statesVal:
                h = heuristics(temp, node.inf, target)
                s = 2 if h == 0 else 0
                if h == 0 and node.inf != target:
                    newNode = TreeNode(temp, node.inf, 1, h, node.cost + 1)
                    possibleStates.append(newNode)
                    statesVal.append(state)

                    temp[idx] = 0
                    newNode = TreeNode(temp, target, 2, h, node.cost + 2)
                    possibleStates.append(newNode)
                elif h == 0 and node.inf == target:
                    newNode = TreeNode(temp, node.inf, s, h, node.cost + 1)
                    possibleStates.append(newNode)
                else:
                    newNode = TreeNode(temp, node.inf, s, h, node.cost + 1)
                    possibleStates.append(newNode)
                    statesVal.append(state)

    # Drain the pitcher
    for idx, pitcher in enumerate(node.state):
        if pitcher > 0:
            temp = node.state.copy()
            temp[idx] = 0
            state = [temp, node.inf]
            if state not in statesVal:
                h = heuristics(temp, node.inf, target)
                s = 2 if h == 0 else 0
                newNode = TreeNode(temp, node.inf, s, h, node.cost + 1)
                possibleStates.append(newNode)
                statesVal.append(state)

    # Transfer to inf pitcher
    for idx, pitcher in enumerate(node.state):
        tempinf = node.inf
        if pitcher + tempinf <= target:
            temp = node.state.copy()
            temp[idx] = 0
            state = [temp, tempinf + pitcher]
            if state not in statesVal:
                h = heuristics(temp, tempinf + pitcher, target)
                s = 2 if h == 0 else 0
                newNode = TreeNode(temp, tempinf + pitcher, s, h, node.cost + 1)
                possibleStates.append(newNode)
                statesVal.append(state)

    # Transfer to other pitcher
    for idx, pitcher in enumerate(node.state):
        for i in range(0, len(node.state)):
            if i == idx:
                continue
            if node.state[i] < capacity[i]:
                temp = node.state.copy()
                water_to_pour = min(pitcher, capacity[i] - node.state[i])
                temp[i] += water_to_pour
                temp[idx] -= water_to_pour
                state = [temp, node.inf]
                if state not in statesVal:
                    h = heuristics(temp, node.inf, target)
                    s = 2 if h == 0 else 0
                    if h == 0 and node.inf != target:
                        if temp[i] + node.inf == target:
                            newNode = TreeNode(temp, node.inf, 1, h, node.cost + 1)
                            possibleStates.append(newNode)
                            statesVal.append(state)
                        else:
                            newNode = TreeNode(temp, node.inf, 1, h, node.cost + 1)
                            possibleStates.append(newNode)
                            statesVal.append(state)

                            temp[idx] = 0
                        newNode = TreeNode(temp, target, 2, h, node.cost + 2)
                        possibleStates.append(newNode)
                    elif h == 0 and node.inf == target:
                        newNode = TreeNode(temp, node.inf, s, h, node.cost + 1)
                        possibleStates.append(newNode)
                    else:
                        newNode = TreeNode(temp, node.inf, s, h, node.cost + 1)
                        possibleStates.append(newNode)
                        statesVal.append(state)
    # Transfer from inf pitcher to other pitchers
    for idx, pitcher in enumerate(node.state):
        if node.inf > 0 and pitcher < capacity[idx]:
            temp = list(node.state)
            temp[idx] = temp[idx] + node.inf
            tempinf = 0
            state = [temp, tempinf]
            if state not in statesVal:
                h = heuristics(temp, tempinf, target)
                s = 2 if h == 0 else 0
                if h == 0 and sum(temp) == target:
                    newNode = TreeNode(temp, tempinf, 2, h, node.cost + 1)
                    possibleStates.append(newNode)
                    statesVal.append(state)
                else:
                    newNode = TreeNode(temp, tempinf, s, h, node.cost + 1)
                    possibleStates.append(newNode)
                    statesVal.append(state)
    return [statesVal, possibleStates]


def pitcherGameMinSteps(data):
    solution = -1
    capacity = data[0]
    target = data[1]
    states = []
    initialState = []
    for i in capacity:
        initialState.append(0)
    root = TreeNode(initialState,0,0,sum(capacity)-target,0)
    tree = Tree(root)
    states.append([initialState,0])
    while endConditionNotReached(tree):
        minNode = min(filter(lambda x: x.stopstate == 0, tree.leaf_nodes), key=lambda x: x.cost + x.heuristic)
        [states, possibilities] = possibleCombinations(minNode, states, capacity, target)
        tree.update_node_stopState(minNode,1)
        for p in possibilities:
            tree.add_node(minNode,p)
    solutionFlag = False
    solutionSet = sys.maxsize
    for node in tree.leaf_nodes:
        if node.stopstate == 2:
           solutionFlag = True
           if node.cost<solutionSet:
               solutionSet=node.cost
    if solutionFlag:
        solution = solutionSet
    return solution

def main():
    if len(sys.argv) <= 1:
        return
    else:
        filename = sys.argv[1]
        if ".txt" in filename:
            if len(sys.argv) < 2:
                return
            else:
                print("Shortest path : ",pitcherGameMinSteps(getData(filename)))

if __name__ == '__main__':
    main()
