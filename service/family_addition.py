from model.family import family_tree
from model.female import Female
from model.male import Male
from model.person import Person


def add_child(person_name: str, child_name: str, gender: str) -> str:
    if person_name in family_tree:
        person = family_tree[person_name]
        if isinstance(person, Male):
            return 'CHILD_ADDITION_FAILED'
        else:
            child = create_person(name=child_name, gender=gender)
            person.children.append(child)
            child.mother = person
            family_tree[child.name] = child
            return 'CHILD_ADDITION_SUCCEEDED'
    else:
        return 'PERSON_NOT_FOUND'


def add_husband(person_name: str, husband_name: str) -> str:
    if person_name in family_tree:
        person = family_tree[person_name]
        if isinstance(person, Male):
            return 'HUSBAND_ADDITION_FAILED'
        else:
            husband = create_person(name=husband_name, gender='Male')
            person.husband = husband
            husband.wife = person
            family_tree[husband.name] = husband
            return 'HUSBAND_ADDITION_SUCCEEDED'
    else:
        return 'PERSON_NOT_FOUND'


def add_wife(person_name: str, wife_name: str) -> str:
    if person_name in family_tree:
        person = family_tree[person_name]
        if isinstance(person, Female):
            return 'WIFE_ADDITION_FAILED'
        else:
            wife = create_person(name=wife_name, gender='Female')
            person.wife = wife
            wife.husband = person
            family_tree[wife.name] = wife
            return 'WIFE_ADDITION_SUCCEEDED'
    else:
        return 'PERSON_NOT_FOUND'


def create_person(name: str, gender: str) -> Person:
    if gender == 'Male':
        return Male(name)
    elif gender == 'Female':
        return Female(name)
