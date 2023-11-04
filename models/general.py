from models.person import Job, Person


class Organization:
    def __init__(
        self,
        name: str,
        description: str,
        participants: list = None,
        leader: Person = None,
    ):
        self.name = name
        self.description = description
        self.participants = []
        self.leader = leader


class Relationship:
    def __init__(self, person: Person, relationship_type: str):
        self.person = person
        self.relationship_type = relationship_type


class Guild:
    def __init__(
        self,
        name: str,
        description: str,
        participants: list = None,
        leader: Person = None,
        job: Job = None,
    ):
        self.name = name
        self.description = description
        self.job = job
        self.participants = participants
        self.leader = leader


class Group:
    def __init__(
        self,
        name: str,
        description: str,
        participants: list = None,
        leader: Person = None,
    ):
        self.name = name
        self.description = description
        self.participants = participants
        self.leader = leader


class Faction:
    def __init__(
        self,
        name: str,
        description: str,
        participants: list = None,
        leader: Person = None,
    ):
        self.name = name
        self.description = description
        self.participants = []
        self.leader = leader
