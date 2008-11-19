#include "albool.h"

AlBool::AlBool(bool val) {
    this->value = val;
}

AlBool::AlBool() {
    this->value = false;
}

AlBool::operator bool() {
    return this->value;
}
