"""
Created on Thu Mar 7 2024, 08:08 PM

@author: uchukwu
"""

class DFA:

    def __init__(self, Q, Sigma, delta, q0, F):
        """
        Initialize a deterministic finite automaton (DFA) object.

        Args:
            Q (set): Set of states in the DFA.
            Sigma (set): Set of symbols (alphabet) accepted by the DFA.
            delta (dict): Transition function mapping (state, symbol) pairs to the next state.
                        It is a dictionary where keys are tuples (state, symbol) and values are states.
            q0: Initial state of the DFA.
            F (set): Set of final states (accepting states) in the DFA.

        Note:
            The transition function 'delta' should be a dictionary where each key is a tuple
            (current_state, input_symbol) and the corresponding value is the next state
            reached after transitioning from 'current_state' on input 'input_symbol'.
        """
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def __repr__(self):
        """
        Return a string representation of the deterministic finite automaton (DFA) object.

        Returns:
            str: String representation of the DFA, displaying its attributes.

        Note:
            This method provides a human-readable representation of the DFA object,
            showing its set of states, alphabet, transition function, initial state, and final states.
        """
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    def run(self, w):
        """
        Run the deterministic finite automaton (DFA) on the input string w.

        Args:
            w (str): The input string to be processed by the DFA.

        Returns:
            bool: True if the DFA accepts the input string w, False otherwise.

        Note:
            This method simulates the behavior of the DFA on the input string w.
            It starts from the initial state and transitions according to the symbols
            in the input string w, updating the current state until the end of the string is reached.
            The final result indicates whether the DFA ends in an accepting state or not.
        """
        q = self.q0

        while w != "":
            q = self.delta((q, w[0]))
            w = w[1:]

        return q in self.F


## Example
# 
# D0 = DFA({0,1,2}, 
#             {"a","b"}, 
#             {(0,"a") : 0, (0,"b") : 1, (1,"a") : 2, (1,"b") : 1, (2,"a") : 2, (2,"b") : 2},
#             0,
#             {0,1})
# 
# D0.run("aa")
# D0.run("aabbb")
