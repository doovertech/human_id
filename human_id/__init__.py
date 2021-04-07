import random
import itertools
from typing import Hashable
from . import dictionary

__all__ = ["generate_id"]

system_random = random.SystemRandom()


def generate_id(separator="-", seed: Hashable = None, word_count=4) -> str:
    """
    Generate a human readable ID

    :param separator: The string to use to separate words
    :param seed: The seed to use. The same seed will produce the same ID
    :param word_count: The number of words to use. Minimum of 2.
    :return: A human readable ID
    """
    if word_count < 2:
        raise ValueError("word_count cannot be lower than 2")

    random_obj = system_random
    if seed:
        random_obj = random.Random(str(seed))

    parts = {dictionary.adjectives: 1, dictionary.nouns: 1, dictionary.verbs: 0 }

    for _ in range(2, word_count):
        parts[random_obj.choice(list(parts.keys()))] += 1

    parts = itertools.chain.from_iterable(
        random_obj.sample(part, count) for part, count in parts.items()
    )

    return separator.join(parts)
