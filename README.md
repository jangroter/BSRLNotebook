# BSRLNotebook

In this Jupyter notebook, we will take a look at how to use Deep Reinforcement Learning (DRL) in conjunction with the Bluesky Open Air Traffic Simulator. 
The task of the DRL agent is to learn to maintain a level flight before initiating descent such that the total reward during the flight is maximized. 

This example uses the Soft Actor Critic algorithm (Haarnoja et al., 2018) implement via Pytorch, if however the function names are adhered, any DRL algorithm could be utilized.

**To run the example the following packages are required:**  
pip install bluesky-simulator[full]  
https://pytorch.org/get-started/locally/ -> follow this for your operating system  



(Haarnoja at al., 2018) : Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018, July). Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In International conference on machine learning (pp. 1861-1870). PMLR.
