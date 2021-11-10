# CartPole-v0:
A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the center.

More description about this game can be found in [open AI gym](https://gym.openai.com/envs/CartPole-v0/) <br>

You are required to balance the cartpole for as long as possible, but for simplicity, let's balance it for 500 time steps. So, the maximum length of the episode is 500 timesteps. The episode ends before 500 timesteps if the pole falls off.

## Environment

**Stae/ Observation**

Num| Obsrevation| Minimum Value| Maximmum Value|
---|---|---|---|
0| Cart Position| -4.8| 4.8|
1| Cart Velocity| -Inf | Inf|
2| Pole angle|$~-41.8^\circ$| $~41.8^\circ$|
3| Pole velocity at tip| -Inf| Inf|

**Actions**

Num| Action|
---|---|
0| Push cart to the left|
1| Push cart to the right|

**Reward**

Reward is 1 for evary step taken , including terminal state

**Initial state**

Here, the state is represented by 4 values (Cart Position, Cart Velocity, Pole Angle, Pole Velocity at Tip). All observations are assigned a uniform random value 

**Episode Termination**
1. Pole angle is more than $\pm{12}^\circ$
2. cart position is more tha $\pm{2.4}$
3. Episode length is greater than 200
