from binaryninja import load as load_bv
from binaryninja import lowlevelil
import sys

if len(sys.argv)<2:
    print("need libc")
    exit()

libc = sys.argv[1]

bv = load_bv(libc,options={"analysis.mode":"controlFlow"})
print("loaded")
end = bv.get_section_by_name(".got.plt").end
addr = bv.get_section_by_name(".got.plt").start

while addr < end:
    var = bv.get_next_data_var_after(addr)
    sym = bv.get_symbol_at(var.value)
    if sym is not None and var.value !=0:
        sym_name = "jump_"+sym.name
        for ref in bv.get_code_refs(var.address):
            ref.function.analysis_skipped=False
            bv.update_analysis_and_wait()
            llil = ref.function.get_llil_at(ref.address)
            if isinstance(llil, lowlevelil.LowLevelILJump):
                ref.function.name = sym_name
                for next_ref in bv.get_code_refs(ref.function.start):
                    bb = next_ref.function.get_basic_block_at(next_ref.address)
                    print(f"{hex(bb.start)}: ",end="")
                    for line in bb.disassembly_text:
                        print(str(line).replace("    ",""),end="; ")
                        if line.address >= next_ref.address:
                            print("")
                            break
                    # __import__("IPython").embed()
    addr = var.address