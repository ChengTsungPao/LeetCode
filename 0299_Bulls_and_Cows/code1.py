class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = sum([d1 == d2 for d1, d2 in zip(secret, guess)])
        B = sum((collections.Counter(secret) & collections.Counter(guess)).values()) - A
        return "{}A{}B".format(A, B)