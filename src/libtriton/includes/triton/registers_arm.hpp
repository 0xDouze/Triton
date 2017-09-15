#ifndef REGISTERS_ARM_H_
#define REGISTERS_ARM_H_

namespace triton {
    namespace arch {
        enum registers_arm {
            ID_REG_INVALID = 0,
#define REG_SPEC(UPPER_NAME, LOWER_NAME, THUMB_AVAIL) \
            ID_REG_##UPPER_NAME,
            #define REG_SPEC_NO_CAPSTONE REG_SPEC
            #include "arm.spec"
        }
    }
}

#endif /*  !REGISTERS_ARM_H_ */
