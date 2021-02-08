import unicorn
import keystone
import capstone

from ..architecture import SimpleArchitecture, Endian
from ..regs import RegisterSet


ARM64_REGS = RegisterSet.from_libs('arm64')

ARCH_ARM64 = SimpleArchitecture(
    name='arm64',
    alt_names=['aarch64', 'armv8'],
    bits=64,
    endian=Endian.LITTLE,
    insn_alignment=4,
    min_insn_size=4,
    max_insn_size=4,
    regs=ARM64_REGS,
    pc_name='pc',
    sp_name='sp',
    retval_name='x0',
    retaddr_name='lr',
    ks_arch=keystone.KS_ARCH_ARM64,
    cs_arch=capstone.CS_ARCH_ARM64,
    uc_arch=unicorn.UC_ARCH_ARM64
)
ISA_ARM64 = ARCH_ARM64.isa
ARCH_ARM64.add_to_db()