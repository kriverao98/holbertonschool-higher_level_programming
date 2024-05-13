#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple containing the length of
    the sentence and its first character.
    """
    if sentence == 0:
        return (None)
    return (len(sentence), sentence[0])
