# VisualizeComputerCommunications
A series of functions that had helped me visualize some concepts in my computer communications textbook.

** ConnectionDropPoisson.py **
Shows the poisson distribution with different lambda values, that are supposed to closely resemble the events of dropped packets in a network relationship between two devices.

** SurvivorHazardFuncsVisual.py **
Generates two graphs that detail the Survivor and Hazard functions that is used to model relationships when considering survival analysis, this example was used to detail the odds of a reciever dropping a packet.

** SwitchingElementProblem.py **
Simulate the discrete event of a switching element with 10 inputs and outputs. Where each input follows a Bernoulli process describing the probability of a packet arriving. If less than 3 elements arrive at the input they are all forwarded to the output of the lement. Otherwise only three packets are chosen at random to be fowarded to the output untill the queue ends.
