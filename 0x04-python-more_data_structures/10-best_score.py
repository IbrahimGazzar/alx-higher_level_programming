#!/usr/bin/python3
def best_score(a_dictionary):
    score = None
    winner = None
    if a_dictionary:
        for i in a_dictionary.keys():
            if not score or a_dictionary[i] > score:
                winner = i
                score = a_dictionary[i]
    return winner
