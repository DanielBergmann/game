class Quest:
    def __init__(self, name: str, description: str, reward: float = 0.0):
        self.name = name
        self.description = description
        self.reward = reward
