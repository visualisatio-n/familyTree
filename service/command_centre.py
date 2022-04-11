from exception.exceptions import CommandNotValidException, PersonNotFoundException
from service.family_addition import add_child
from service.relation_finder import RelationFinder


class CommandCentre:
    @classmethod
    def run_command(cls, command_line: str):
        command_components = command_line.split(' ')
        command = command_components[0]
        if command == 'ADD_CHILD':
            cls.run_add_child(command_components[1:])
        elif command == 'GET_RELATIONSHIP':
            cls.run_get_relationship(command_components[1:])
        else:
            raise CommandNotValidException(f'{command} is not valid')

    @classmethod
    def run_add_child(cls, command_components):
        print(add_child(person_name=command_components[0], child_name=command_components[1],
                        gender=command_components[2]))

    @classmethod
    def run_get_relationship(cls, command_components):
        try:
            res = RelationFinder.get_relation(person_name=command_components[0], relation=command_components[1])
            if res:
                print(" ".join(res))
            else:
                print('None')
        except PersonNotFoundException as e:
            print('PERSON_NOT_FOUND')
