# -*- coding: utf-8 -*-
"""Agent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gG7f1ouBJGmg0VfcMm9JRcUfmy6EVm8u
"""

# Libraries
import numpy as np
import random
import collections
from collections import deque

# Libraries for DQN model
import keras
from keras import layers, Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam


# Create the Agent class

class CartpoleAgent():

  def __init__(self, action_size, state_size, discount_factor=0.95, learning_rate=0.01,
               epsilon=1, epsilon_decay=0.99, epsilon_min=0.01):
    #parameters

    # State and action size
    self.action_size= action_size
    self.state_size= state_size

    #Hyperparameters
    self.discount_factor= discount_factor
    self.learning_rate= learning_rate
    self.epsilon= epsilon
    self.epsilon_decay= epsilon_decay
    self.epsilon_min= epsilon_min

    # Batch size 50 and dynamic memory size 2000
    self.batch_size= 50
    self.memory= deque(maxlen=2000)

    # DQN
    self.model= self.build_model()

  def build_model(self):
    """
    Build DQN as function approximater for Q(s,a)
    """

    input_shape= self.state_size
    output_shape = self.action_size

    model= Sequential()
    #input layer
    model.add(Dense(32, input_dim=self.state_size, activation='relu'))
    #hidden layer
    model.add(Dense(32, activation='relu'))
    #output layer
    model.add(Dense(self.action_size,activation='relu' ))
    # Error calculation
    model.compile(loss='mse', optimizer= Adam(lr=self.learning_rate))

    return model

  def get_action(self, state):
    """
    Create a epsilon greey action policy
    """
    if np.random.rand() < self.epsilon:
      # explore: draw a random action : 0 or 1
      return random.randrange(self.action_size)
    else:
      state= state.reshape(1, self.state_size) # In keras by default the input is batch_size, not to confuse with minibatch size
      q_value= self.model.predict(state)
      return np.argmax(q_value[0])

  def append_sample(self, state, action, reward, next_state, done):
    """
    Add new experience to memory
    """
    self.memory.append((state, action, reward, next_state, done))

  def train_model(self):
    """
    Train the DQN for a mini batch. Input is state and output is
    q-value for each action. Target is greedy reward , predicted value in Q(s,a)
    """
    #Start training once memeory is more than batch_size
    if len(self.memory)> self.batch_size:

      #sample mini batch
      minibatch = random.sample(self.memory, self.batch_size)

      #initialize - current state and next_state
      current_state = np.zeros((self.batch_size, self.state_size))
      next_state= np.zeros((self.batch_size, self.state_size))

      actions, rewards, done = [], [], []

      # Store separately from a minibatch from memory
      for i in range(self.batch_size):
        state, action, reward, update_state, done_boolean = minibatch[i]

        current_state[i] = state 
        next_state[i] = update_state
        actions.append(action)
        rewards.append(reward)
        done.append(done_boolean)

      # Predict q-values Q(s,a)
      target= self.model.predict(current_state)

      # Q value for next state required for target q_value from temporal difference algorithm
      target_q_value= self.model.predict(next_state)

      # TD calculated Q value
      for i in range(self.batch_size):
        if done[i]:
          target[i][actions[i]]= rewards[i] # For terminal state
        else:
          target[i][actions[i]] = rewards[i] + self.discount_factor * np.max(target_q_value[i]) # calculate r + gamma* max_over_actions Q(next_state, action)
      
      #model fit
      self.model.fit(current_state, target, batch_size= self.batch_size, epochs=1, verbose=0)

  def save_model_weights(self, name):
    self.model.save_weights(name)