# Retry logic with backoff

import time
import random

def retry_with_backoff(func, max_retries=5, base_delay=1):
    retries = 0

    while retries < max_retries:
        try:
            return func()
        except Exception as e:
            retries += 1
            if retries == max_retries:
                raise  # re-raise last exception

            delay = base_delay * (2 ** (retries - 1))
            print(f"Retry {retries} failed. Retrying in {delay}s...")
            time.sleep(delay)


def unstable_api():
    if random.random() < 0.7:
        raise Exception("API failed")
    return "Success"

print(retry_with_backoff(unstable_api))
