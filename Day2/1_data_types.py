''' How Python Works ?
1. First we create a file (program.py)
2. Then the program is compiled (program.pyc) This is in the Bite-Code format
3. Then a PVM(Python Virtual Machine) is generated
4. Bite-Code lai PVM le Machine Code ma change Garxa (line-by-line) in the form which Computer Processor understands
5. Program run vaepaxi aani output devices haru le output dinxa in the human readable and form  
'''

print("My name is Samundra")

# Variable and Data Types
name = "Samundra Khanal" # String
print(name,type(name))

num = 4 #integer
print(num,type(num),id(num))

grade = 4.6 # Floating point
print(grade,type(grade))

complex_data = 3 + 4j #Complex Numbers
print(complex_data,type(complex_data))

checked = True # Boolean 
print(checked, type(checked))

value = None
print(value, type(value))