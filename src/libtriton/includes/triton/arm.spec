#pragma warning(disable:4067)

#if not (defined REG_SPEC || defined REG_SPEC_NO_CAPSTONE)
#error REG_SPEC have to be specified before including specs
#endif

//REG_SPEC(UPPER_NAME, LOWER_NAME, THUMB_AVAIL)

/* GPR 32 bits */
REG_SPEC(R0, r0, true, true) //!< r0
REG_SPEC(R1, r1, true, true) //!< r1
REG_SPEC(R2, r2, true, true) //!< r2
REG_SPEC(R3, r3, true, true) //!< r3
REG_SPEC(R4, r4, true, true) //!< r4
REG_SPEC(R5, r5, true, true) //!< r5
REG_SPEC(R6, r6, true, true) //!< r6
REG_SPEC(R7, r7, true, true) //!< r7
REG_SPEC(R8, r8, false, true) //!< r8
REG_SPEC(R9, r9, false, true) //!< r9
REG_SPEC(R10, r10, false, true) //!< r10
REG_SPEC(R11, r11, false, true) //!< r11
REG_SPEC(R12, r12, false, true) //!< r12

REG_SPEC(R13, r13, false, true) //!< r13
REG_SPEC(R14, r14, false, true) //!< r14
REG_SPEC(R15, r15, false, true) //!< r15

REG_SPEC(SP, sp, true, false) //!< sp
REG_SPEC(LR, lr, true, false) //!< lr
REG_SPEC(PC, pc, true, false) //!< pc

/* status register */
REG_SPEC(CPSR, cpsr, true, true) //!< cpsr

/* Exception mode - Saved status register */
REG_SPEC(SPSR, spsr, false, true)
