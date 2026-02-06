# Rate limiter

import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)

    def allow_request(self, key):
        now = time.time()
        window_start = now - self.window_seconds

        # Remove old timestamps
        self.requests[key] = [
            t for t in self.requests[key] if t > window_start
        ]

        if len(self.requests[key]) < self.max_requests:
            self.requests[key].append(now)
            return True

        return False


rl = RateLimiter(3, 10)

for i in range(5):
    print(rl.allow_request("user_1"))
    time.sleep(1)
