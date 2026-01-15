import random

def generate_traffic(slice_type):
    if slice_type == "eMBB":
        return random.randint(50, 100)
    elif slice_type == "URLLC":
        return random.randint(5, 20)
    elif slice_type == "mMTC":
        return random.randint(1, 10)
