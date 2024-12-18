
import secrets as secrets
from functools import cache as function_cache, wraps
import random
from numpy.random import SeedSequence, Generator, Philox


def soft_random(size: int = 0x2540BE3FF) -> int:
    """
    Generate a deterministic random number using philox\n
    :params size: `int` RNG ceiling in hex format
    :returns: `int` a random number of the specified length\n
    pair with `random.seed()` for best effect
    """
    entropy = f"0x{secrets.randbits(128):x}"  # good entropy
    rndmc = Generator(Philox(SeedSequence(int(entropy, 16))))
    return int(rndmc.integers(0, size))


def hard_random(hardness: int = 5) -> int:
    """
    Generate a cryptographically secure random number\n
    :param hardness: `int` byte length of generated number
    :returns: `int` Non-prng random number
    """
    return int(secrets.token_hex(hardness), 16)  # make hex secret be int