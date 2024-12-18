import re

#input
registers, program = open("input.txt").read().strip().split("\n\n")
registers = {label: int(value) for label, value in \
                re.findall(r"Register (\w): (\d+)", registers)}
program = [int(i) for i in program[9:]]

#process
pointer_idx = 0
out = []

while pointer_idx < len(program) - 1:
    combo_operands = {0:0,
                      1:1,
                      2:2,
                      3:3,
                      4:registers["A"],
                      5:registers["B"],
                      6:registers["C"]}

    curr_opcode = program[pointer_idx]
    curr_operand = program[pointer_idx+1]

    if curr_opcode == 0: #adv
        result = registers["A"] // (2**combo_operands[curr_operand])
        registers["A"] = result

    elif curr_opcode == 1: #bxl
        result = registers["B"] ^ curr_operand
        registers["B"] = result
        
    elif curr_opcode == 2: #bst
        result = combo_operands[curr_operand] % 8
        registers["B"] = result
        
    elif curr_opcode == 3: #bxl
        if registers["A"] != 0: pointer_idx = curr_operand - 2
        #account for offset

    elif curr_opcode == 4: #bxc
        result = registers["B"] ^ registers["C"]
        registers["B"] = result
        
    elif curr_opcode == 5: #out
        result = combo_operands[curr_operand] % 8
        out.append(str(result))
    
    elif curr_opcode == 6: #bdv
        result = registers["A"] // (2**combo_operands[curr_operand])
        registers["B"] = result

    elif curr_opcode == 7: #cdv
        result = registers["A"] // (2**combo_operands[curr_operand])
        registers["C"] = result

    pointer_idx += 2
print(",".join(out))