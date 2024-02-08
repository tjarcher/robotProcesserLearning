# robotProcesserLearning

Part of Master Project for Tim Archer at Montclair State University

Program designed to find optimal process for a robot to pick up and assemble 8 pieces of a toy car

sequenceRun.py is used to gather data
Code randomly picks an available piece
User grades the appropriateness of grabbing that piece at that time on a scale of -10 to 10
Repeats until all pieces are picked
Data saved in results.txt file (created if not present)

markovChain.py tells the optimal path based on currently gathered data
Reads data saved to results.txt and determines best currently available path
