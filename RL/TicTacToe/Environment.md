# Design of the environment (refer .py file)

A class object is created to add all the necessry calculations to simulate a *Numerical Tic-Tac-Toe* game. This will be used further to generate Q-values using a Q-learning algorithm.
Logic of different components are briefly explained in text.<br>

**Function name: *is_winning*** <br>
In order to evaluate the result of the game at any step, the sum in one direction (row/ column or diagonal) will be evaluated.
If we consider the a 3 x 3 board positions by indexes 0 to 8 , then only following combinations needs to be evaluated:
- Row sums : Position by index - (0,1,2), (3,4,5), (6,7,8)
- Column sumns : Position by index - (0,3,6), (1,4,7), (2,5,8)
- Diagonal sums : positions by index - (0,4,8), (2,4,6)
Also we need to ensure , while computing this sum , none of the index position is blank and the sum is exactly 15 in order to decalre win.

**Function name: *is_terminal*** <br>
Two terminal states:
- Win the game , i.e is_winning function returns True
- Tie: i.e. there is no more blank position in the board

**Function name: *allowed_positions*** <br>
All available blank positions in the board

**Function name: *allowed_values*** <br>
Each value can be used only once.
- Allowed values at initial state [1,2,3,4,5,6,7,8,9]
- None of the values that are already available in the board
- Agent can use only odd values that are not available in the board
- environment/ player2 can choose from even values that are not available in the board

**Function name: *action_space*** <br>
Action is a combination of alloed values and available blank spaces in the board

**Function name: *state_transition*** <br>
Takes current state and action and returns the board position just after agent's move.
Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]

**Function name: *step*** <br>
Note that a step is essentially one attempt from agent and environment.
This is performed by a sequence of steps:
1. As 1st part of the step , the agent performs an action as selectiong a number from available set of unused odd numbers and puts down to available blank spots in the board. 
2. Check the new state results in a Win (reward 10) to RL agent or tie (reward 0). Otherwise continue the game
3. If it is not a win by agent , then environment selects one of the unused even numbers and puts down at any of the available blank spaces.
4. Check the new state results in a Win (reward 10) by environment or tie (reward 0). Otherwise continue the game
5. Reward for a single step is -1
