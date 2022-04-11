import sys
from service.command_centre import CommandCentre
from service.family_addition import add_child, add_wife, add_husband

add_child(person_name='Queen Anga', child_name='Chit', gender='Male')
add_child(person_name='Queen Anga', child_name='Ish', gender='Male')
add_child(person_name='Queen Anga', child_name='Vich', gender='Male')
add_child(person_name='Queen Anga', child_name='Aras', gender='Male')
add_child(person_name='Queen Anga', child_name='Satya', gender='Female')

add_wife(person_name='Chit', wife_name='Amba')
add_wife(person_name='Vich', wife_name='Lika')
add_wife(person_name='Aras', wife_name='Chitra')
add_husband(person_name='Satya', husband_name='Vyan')

add_child(person_name='Amba', child_name='Dhrita', gender='Female')
add_child(person_name='Amba', child_name='Tritha', gender='Female')
add_child(person_name='Amba', child_name='Vritha', gender='Male')
add_child(person_name='Lika', child_name='Vila', gender='Female')
add_child(person_name='Lika', child_name='Chika', gender='Female')
add_child(person_name='Chitra', child_name='Jnki', gender='Female')
add_child(person_name='Chitra', child_name='Ahit', gender='Male')
add_child(person_name='Satya', child_name='Asva', gender='Male')
add_child(person_name='Satya', child_name='Vyas', gender='Male')
add_child(person_name='Satya', child_name='Atya', gender='Female')

add_husband(person_name='Dhrita', husband_name='Jaya')
add_husband(person_name='Jnki', husband_name='Arit')
add_wife(person_name='Asva', wife_name='Satvy')
add_wife(person_name='Vyas', wife_name='Krpi')


add_child(person_name='Dhrita', child_name='Yodhan', gender='Male')
add_child(person_name='Jnki', child_name='Laki', gender='Male')
add_child(person_name='Jnki', child_name='Lavnya', gender='Female')
add_child(person_name='Satvy', child_name='Vasa', gender='Male')
add_child(person_name='Krpi', child_name='Kriya', gender='Male')
add_child(person_name='Krpi', child_name='Krithi', gender='Female')

file_path = sys.argv[1]
command_centre = CommandCentre()
with open(file_path, 'r') as file:
    for line in file:
        command_centre.run_command(command_line=line.rstrip())




