"""Utility functions used by the SCAN-IDS generator."""
import random
import numpy as np

def seed_everything(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    return random.Random(seed)

def sample_u8(rng, low=0, high=255):
    return rng.randint(low, high)

def bounded_noise(value, rng, amount=5):
    return max(0, min(255, int(value) + rng.randint(-amount, amount)))

def format_can_id(can_id):
    return f"{int(can_id):04X}"

def make_payload(baseline, rng, noise=5):
    return [bounded_noise(v, rng, noise) for v in baseline]

def optional_public_dataset_loader(path):
    """Load a user-supplied CSV containing CAN ID/payload columns if needed."""
    import pandas as pd
    return pd.read_csv(path)
