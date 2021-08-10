import angr
import claripy

flag_found = False
for q in range(10,126):
    FLAG_LEN = q
    STDIN_FD = 0

    base_addr = 0x100000 # To match addresses to Ghidra

    proj = angr.Project("./verybabyrev", main_opts={'base_addr': base_addr}) 

    flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(FLAG_LEN)]
    flag = claripy.Concat( *flag_chars + [claripy.BVV(b'\n')]) # Add \n for scanf() to accept the input

    state = proj.factory.full_init_state(
            args=['./verybabyrev'],
            add_options=angr.options.unicorn,
            stdin=flag,
    )

    simgr = proj.factory.simulation_manager(state)
    find_addr  = 0x101332 # SUCCESS
    avoid_addr = (0x1012C5, 0x101348) # FAILURE
    simgr.explore(find=find_addr, avoid=avoid_addr)

    if (len(simgr.found) > 0):
        for found in simgr.found:
            print(found.posix.dumps(STDIN_FD))
            flag_found = True
            break
    if flag_found == True:
        break
    else:
        print("angr failed to find a path to the solution :(")