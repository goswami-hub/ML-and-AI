# -*- coding: utf-8 -*-
"""env_v00.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12wivgtlmsIHFcixv6EjCHXI-PV55opsq
"""

# Import Libraries
import numpy as np
import math
import random

# Hyperparameters

m=5 # Number of cities
t=24 # Hours in a day
d=7 # days in a week
C=5 # Fuel cost per hour
R=9 # Revenue from a passenger per hour


class CabDriver():

  def __init__(self):
    """ define state and action space , also initialize state"""
    self.action_space = [[p,q] for p in range(m) for q in range(m) if p!=q or p==0 ] # [0,0] is offline
    self.state_space = [[x,y,z] for x in range(m) for y in range(t) for z in range(d)] # All possible states
    self.state_init = random.choice(self.state_space)    # randomly initialize state

    # Start of an episod
    self.reset()

  #Encoding input for NN
  #Architecture 1 : Input is state output is Q value for each state action pair
  def state_encod_arch1(self, state):
    """convert the state to a vector so that it can be fed into the NN as one hot encoded vector if we are using architecture 1.
    with m posible places , t possible hours and d possible days size of the vector (m+t+d)x1 """
    l= m+t+d
    state_encod=[0]*l #create a list of 0s of length l 
    state_encod[state[0]]=1 # place
    state_encod[m+state[1]]=1 # time
    state_encod[m+t+state[2]] = 1 # day

    return state_encod
  #Architecture 2 : Input is state and action output is Q value for given state and action
  def state_encod_arch2(self, state, action):
    """convert state, action pair to a one hot encoded vector for input to NN if we are using architecture 2.
    with m posible places , t possible hours and d possible days size of the vector [(m+t+d)+(m+m)]x1 """
    l= m+t+d+m+m
    state_encod=[0]*l #create a list of 0s of length l 
    state_encod[state[0]]= 1 # initial place
    state_encod[m+state[1]]= 1 # time
    state_encod[m+t+state[2]] = 1 # day
    state_encod[m+t+d+action[0]] = 1 #pick-up
    state_encod[m+t+d+m+action[1]] = 1 #drop

    return state_encod

  def requests(self,state):
    """Determining the number of requests based on current location of the driver"""

    loc= state[0] #Location

    if loc== 0:
      requests= np.random.poisson(2)
    elif loc== 1:
      requests= np.random.poisson(12)
    elif loc== 2:
      requests= np.random.poisson(4)
    elif loc== 3:
      requests= np.random.poisson(7)
    else:
      requests= np.random.poisson(8)

    if requests>15:
      requests=15
    # Collect random actions as per number number of requests received
    possible_actions_index= random.sample(range(1, (m-1)*m+1), requests) # (0,0) is not considered as customer request

    actions= [self.action_space[i] for i in possible_actions_index]

    if [0,0] not in actions:
      actions.append([0,0]) #always offline or no request should be available as an action 
      possible_actions_index.append(0) # Position of (0,0) is 0 in action_space

    return possible_actions_index, actions 

  def time_after_travel(self, time, day, travel_time):
    """ Calculate new time after a trip"""
    travel_time=int(travel_time) # Only integer time in hour is acceptable
    curr_time= time #Time of the day 0-23
    curr_day = day # day of the week 0-6

    if (curr_time + travel_time) < t:
      curr_time= curr_time + travel_time

    else:
      curr_time = (curr_time + travel_time) % t # If time passes 23 adjust it to 0-23

      days = (curr_time + travel_time) // t  # calculate the number of days passed

      curr_day =  (curr_day + days) % d  # Convert it to 0-6
      
    return curr_time, curr_day
        
  def next_state_func(self, state, action, Time_matrix):
    """Takes state, action and time matrix as input and calculates next step as output"""
    next_state=[]

    curr_loc=state[0]   #Current location
    curr_time= state[1] #Current time
    curr_day = state[2] #Current day

    pick_loc=action[0] #Pickup location
    drop_loc=action[1] #Drop location

    wait_time=0
    transit_time=0
    ride_time=0
    total_time=0

    """
         3 Scenarios: 
           a) Refuse all requests
           b) Driver is already at pick up point
           c) Driver is not at the pickup point.
    """  
      #Scenario 1

    if action==[0,0]:
      wait_time=1
      next_loc= curr_loc
    #Scenario 2
    elif curr_loc==pick_loc:
      ride_time= Time_matrix[curr_loc][drop_loc][curr_time][curr_day]
      next_loc= drop_loc
    #Scenario 3
    else:
      # Driver to travel to pick up
      transit_time= Time_matrix[curr_loc][pick_loc][curr_time][curr_day]
      update_time, update_day = self.time_after_travel(curr_time, curr_day, transit_time)  

      #Driver to travel from pick up to drop
      ride_time= Time_matrix[pick_loc][drop_loc][update_time][update_day]
      next_loc= drop_loc 

    # Calculate total time as sum of all durations
    total_time = (wait_time + transit_time + ride_time)
    next_time, next_day = self.time_after_travel(curr_time, curr_day, total_time)

    next_state= [next_loc, next_time, next_day]

    return next_state, wait_time, transit_time, ride_time
         

  def reward_func(self, state, action, Time_matrix):
    """Takes state, action and time matrix as input and returns reward"""

    next_state, wait_time, transit_time, ride_time= self.next_state_func(state, action, Time_matrix)

    reward= R*ride_time - C*(wait_time+ transit_time+ ride_time)

    return reward

  def step(self, state, action, Time_matrix):
      """
      Summary function returns reward, next state and total time
      """
      # Get the next state and the various time durations
      next_state, wait_time, transit_time, ride_time = self.next_state_func(state, action, Time_matrix)

      # Calculate the reward based on the different time durations
      rewards = self.reward_func(state, action, Time_matrix)
      trip_duration = wait_time + transit_time + ride_time
        
      return rewards, next_state, trip_duration

  def reset(self):
    return self.action_space, self.state_space, self.state_init