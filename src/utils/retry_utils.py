import time
import logging

def retry_with_backoff(func, max_retries=3, backoff_factor=2):
    """Retries a function with exponential backoff on failure."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            logging.error(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(backoff_factor ** attempt)
            else:
                raise e
