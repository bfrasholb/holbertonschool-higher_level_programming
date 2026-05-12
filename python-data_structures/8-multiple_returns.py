#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        return "Length: 0 - First character: None"
    return (len(sentence), sentence[0])
