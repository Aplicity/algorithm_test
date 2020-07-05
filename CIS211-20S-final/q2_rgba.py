"""CIS 211 Final Exam problem.
We always wear our masks.
"""
from typing import Tuple
# Colors are sometimes encoded in a format called
# RGBA, for "Red, Green, Blue, Alpha".
# The first three components (RGB) represent a color,
# as levels 0..255 of a primary color.  The fourth
# component (A) represents transparency, which we can
# also represent as an integer between 0 for transparent
# to 255 for entirely opaque.
#
# The r component is

def rgba_pack(r: int, g: int, b: int, alpha: int) -> int:
    """Pack red, green, blue, alpha into 32 bits"""
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
    assert 0 <= alpha <= 255
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and 0 <= alpha <= 255:
        r_hex = str(hex(r))
        g_hex = str(hex(g))
        b_hex = str(hex(b))
        alpha_hex = str(hex(alpha))
        total_hex="0x"+r_hex[2:4]+g_hex[2:4]+b_hex[2:4]+alpha_hex[2:4]
        return int(total_hex,16)

    return 0  # FIXME


def rgba_unpack(rgba: int) -> Tuple[int, int, int, int]:
    """Unpack rgba into r, g, b, alpha"""

    tmp = str(hex(rgba))
    if tmp is not None:
        return (int("0x"+tmp[2:4],16),int("0x"+tmp[4:6],16),int("0x"+tmp[6:8],16),int("0x"+tmp[8:10],16))

    return (0, 0, 0, 0)  # FIXME


def main():
    """Smoke test (also included in test_rgba.py)"""
    assert rgba_pack(0xAF, 0xBF, 0xCF, 0xF8) == 0xAFBFCFF8
    assert rgba_unpack(0x11223344) == (0x11, 0x22, 0x33, 0x44)

if __name__ == "__main__":
    main()