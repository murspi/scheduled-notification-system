import time

class RateLimiter:
    def __init__(self, cooldown_seconds: int) -> None:
        self.cooldown = cooldown_seconds
        self.last_sent: float | None = None

    def allow(self) -> bool:
        now = time.time()

        if self.last_sent is None:
            self.last_sent = now
            return True
        
        if now - self.last_sent >= self.cooldown:
            self.last_sent = now
            return True
        
        return False