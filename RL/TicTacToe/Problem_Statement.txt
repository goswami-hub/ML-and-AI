# Problem statement 

In this assignment, we need to build an RL agent that learns to play *Numerical Tic-Tac-Toe* game with od-numbers. Purpose is to train the agent uaing Q-learning model. The environment is playing randomly with the agent. Player who puts down exactly 15 points in one direction (row, column or diagonal) wins the game.<br>

**Rules of the game**<br>
- The game will be played on a 3 x 3 grid (i.e. 9 cells) using numbers from 1 to 9. Each number can be used exactly once in the entire grid
- There are two players:
    - Player 1 : The RL agent is given only odd numbers {1,3,5,7,9}
    - Player 2: The environment is given the even numbers {2,4,6,8}
- Each of them takes a turn. The player with odd numbers i.e. player 1 always goes first
- At each round, a player can use one of the unused numbers in available blank spots in the grid
- The objective is to make 15 points in a row, column or diagonal. A player can use opponenet's number in the grid to make 15
- Terminal state: 
    - Win: When any one player makes 15
    - Tie: All the 9 cells are filled with numbers , but there is no result (i.e. none of the player wins
    
**Reward structure** <br>
Reward= 10 if player1/ RL agent wins
Reward= -10 if player 2 wins
Reward= 0 if game ends in a tie
Reward = -1 for every move by player 1/ agent

**Other definitions** <br>
State: Cleraly state is position of the board. If we represent 9 positions sequentially through a list then a board position [1, nan, 3, nan, 4, 6, nan, nan, nan] <br>
Action: An action is defined as an value entered by the player1/ agent in a certain position e.g. [7,5] this means at position 7 a value 5 in entered by the agent. So new position of the board or updated state is [1, nan, 3, nan, 4, 6, nan, 5, nan]


