from exception.exceptions import RelationNotMappedException, PersonNotFoundException
from model.family import family_tree
from model.female import Female
from model.male import Male
from model.person import Person


class RelationFinder:
    @classmethod
    def get_relation(cls, person_name: str, relation: str):
        relation_factory = cls.get_relation_factory()
        if person_name in family_tree:
            person = family_tree[person_name]
        else:
            raise PersonNotFoundException(f'{person_name} not found')

        if relation in relation_factory:
            relation_finder_func = relation_factory[relation]
            return relation_finder_func(person)
        else:
            raise RelationNotMappedException(
                f'{relation} is not mapped in relation finder factory{relation_factory}')

    @classmethod
    def get_relation_factory(cls):
        relation_factory = dict()
        relation_factory['Paternal-Uncle'] = cls.get_parental_uncle
        relation_factory['Maternal-Uncle'] = cls.get_maternal_uncle
        relation_factory['Paternal-Aunt'] = cls.get_parental_aunt
        relation_factory['Maternal-Aunt'] = cls.get_maternal_aunt
        relation_factory['Sister-In-Law'] = cls.get_sister_in_law
        relation_factory['Brother-In-Law'] = cls.get_brother_in_law
        relation_factory['Son'] = cls.get_son
        relation_factory['Daughter'] = cls.get_daughter
        relation_factory['Siblings'] = cls.get_siblings

        return relation_factory

    @classmethod
    def get_parental_uncle(cls, person: Person) -> list[str]:
        father_siblings = person.mother.husband.mother.children if person.mother and person.mother.husband and \
                                                                   person.mother.husband.mother else []
        parental_uncles = [x.name for x in father_siblings if isinstance(x, Male) and person.mother.husband != x]
        return parental_uncles

    @classmethod
    def get_maternal_uncle(cls, person: Person) -> list[str]:
        mother_sibling = person.mother.mother.children if person.mother and person.mother.mother else []
        maternal_uncles = [x.name for x in mother_sibling if isinstance(x, Male)]
        return maternal_uncles

    @classmethod
    def get_parental_aunt(cls, person: Person) -> list[str]:
        father_siblings = person.mother.husband.mother.children if person.mother and person.mother.husband and \
                                                                   person.mother.husband.mother else []
        parental_uncles = [x.name for x in father_siblings if isinstance(x, Female)]
        return parental_uncles

    @classmethod
    def get_maternal_aunt(cls, person: Person) -> list[str]:
        mother_sibling = person.mother.mother.children if person.mother and person.mother.mother else []
        maternal_uncles = [x.name for x in mother_sibling if isinstance(x, Female) and person.mother != x]
        return maternal_uncles

    @classmethod
    def get_sister_in_law(cls, person: Person) -> list[str]:
        siblings = person.mother.children if person.mother else []
        brothers_wives = [x.wife.name for x in siblings if isinstance(x, Male) and x.wife is not None]
        spouse_sister = list()
        if isinstance(person, Male):
            spouse_sibling = person.wife.mother.children if person.wife and person.wife.mother else []
            spouse_sister = [x.name for x in spouse_sibling if isinstance(x, Female) and person.wife != x]
        elif isinstance(person, Female):
            spouse_sibling = person.husband.mother.children if person.husband and person.husband.mother else []
            spouse_sister = [x.name for x in spouse_sibling if isinstance(x, Female)]
        return brothers_wives + spouse_sister

    @classmethod
    def get_brother_in_law(cls, person: Person) -> list[str]:
        siblings = person.mother.children if person.mother else []
        sister_husband = [x.husband.name for x in siblings if
                          isinstance(x, Female) and x.husband is not None]
        spouse_brother = list()
        if isinstance(person, Male):
            spouse_sibling = person.wife.mother.children if person.wife and person.wife.mother else []
            spouse_brother = [x.name for x in spouse_sibling if isinstance(x, Male)]
        elif isinstance(person, Female):
            spouse_sibling = person.husband.mother.children if person.husband and person.husband.mother else []
            spouse_brother = [x.name for x in spouse_sibling if isinstance(x, Male) and person.husband != x]
        return sister_husband + spouse_brother

    @classmethod
    def get_son(cls, person: Person) -> list[str]:
        if isinstance(person, Male) and person.wife:
            return [x.name for x in person.wife.children if isinstance(x, Male)]
        elif isinstance(person, Female):
            return [x.name for x in person.children if isinstance(x, Male)]

    @classmethod
    def get_daughter(cls, person: Person) -> list[str]:
        if isinstance(person, Male) and person.wife:
            return [x.name for x in person.wife.children if isinstance(x, Female)]
        elif isinstance(person, Female):
            return [x.name for x in person.children if isinstance(x, Female)]

    @classmethod
    def get_siblings(cls, person: Person) -> list[str]:
        if person.mother:
            return [x.name for x in person.mother.children if x.name != person.name]
        else:
            return list()


if __name__ == '__main__':
    relation_finder = RelationFinder()
    relation_finder.get_relation('Ish', 'Sister-In-Law')
