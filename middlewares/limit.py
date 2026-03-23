from functools import wraps
import time

class RateLimitExceeded(Exception):
    pass


def rate_limiter(max_requests_per_second):
    interval = 1.0 / max_requests_per_second
    last_called = [0.0]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < interval:
                raise RateLimitExceeded("Rate limit exceeded. Try again later.")
            last_called[0] = time.time()
            return func(*args, **kwargs)

        return wrapper


def daily_limit_middleware(max_daily_requests):
    request_count = {'count': 0}

    def middleware(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request_count['count'] >= max_daily_requests:
                raise RateLimitExceeded("Daily limit exceeded. Try again tomorrow.")
            request_count['count'] += 1
            return func(*args, **kwargs)

        return wrapper

    return middleware


# Usage example
@daily_limit_middleware(max_daily_requests=100)
@rate_limiter(max_requests_per_second=5)
def some_api_call():
    return "API call successful!"