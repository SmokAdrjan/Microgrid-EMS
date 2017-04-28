import numpy as np
from numpy import *
import dataoperation as do
from HouseholdAgent import HouseholdAgent
from Optimization import Variable

agent = HouseholdAgent(id = "001")

agent.optimize()
do.printcolumn(agent.optimizer.results[:, Variable.m_u])

bounds = [[], []]
bounds[0].append(0.5)
bounds[1].append(0.5)

#agent.add_trade_bounds(bounds)
#agent.optimize()
#do.printcolumn(agent.optimizer.results[:, Variable.m_u])


