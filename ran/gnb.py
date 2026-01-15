import random

class gNB:
    def allocate_resources(self, traffic):
        latency = random.uniform(0.5, 50)
        throughput = traffic * random.uniform(0.8, 1.2)
        return latency, throughput
