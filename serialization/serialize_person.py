from models.person import Person


def serialize_person(person: Person):
    return {
        "name": person.name,
        "location": person.location,
        "inventory": person.inventory,
        "connections": {
            "family": person.family,
            "relationships": person.relationships,
        },
        "business": {
            "job": person.job,
            "tasks": person.tasks,
            "events": person.events,
            "event_history": person.event_history,
        },
        "details": {
            "age": person.age,
            "traits": person.traits,
            "abilities": person.abilities,
            "morality": person.morality,
            "morality_history": person.morality_history,
            "stats": person.stats,
        },
        "health": {
            "max_health": person.max_health,
            "current_health": person.current_health,
            "mental_state": person.mental_state,
            "mental_state_history": person.mental_state_history,
        },
        "knowledge": {
            "known_locations": person.known_locations,
            "known_locations_history": person.known_locations_history,
            "known_people": person.known_people,
            "known_things": person.known_things,
            "known_events": person.known_events,
            "known_jobs": person.known_jobs,
            "known_relationships": person.known_relationships,
            "known_quests": person.known_quests,
            "known_factions": person.known_factions,
            "known_guilds": person.known_guilds,
            "known_groups": person.known_groups,
            "known_organizations": person.known_organizations,
        },
    }


def deserialize_person(data):
    person = Person(
        name=data["name"],
        location=data["location"],
        inventory=data["inventory"],
        relationships=data["connections"]["relationships"],
        job=data["business"]["job"],
        tasks=data["business"]["tasks"],
        events=data["business"]["events"],
        event_history=data["business"]["event_history"],
        age=data["details"]["age"],
        family=data["connections"]["family"],
        traits=data["details"]["traits"],
        abilities=data["details"]["abilities"],
        morality=data["details"]["morality"],
        morality_history=data["details"]["morality_history"],
        stats=data["details"]["stats"],
        max_health=data["health"]["max_health"],
        current_health=data["health"]["current_health"],
        mental_state=data["health"]["mental_state"],
        mental_state_history=data["health"]["mental_state_history"],
        known_locations=data["knowledge"]["known_locations"],
        known_locations_history=data["knowledge"]["known_locations_history"],
        known_people=data["knowledge"]["known_people"],
        known_things=data["knowledge"]["known_things"],
        known_events=data["knowledge"]["known_events"],
        known_jobs=data["knowledge"]["known_jobs"],
        known_relationships=data["knowledge"]["known_relationships"],
        known_quests=data["knowledge"]["known_quests"],
        known_factions=data["knowledge"]["known_factions"],
        known_guilds=data["knowledge"]["known_guilds"],
        known_groups=data["knowledge"]["known_groups"],
        known_organizations=data["knowledge"]["known_organizations"],
    )

    return person
