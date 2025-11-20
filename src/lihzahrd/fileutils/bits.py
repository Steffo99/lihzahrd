BITS = {
    i: (
        bool(i & 0b0000_0001),
        bool(i & 0b0000_0010),
        bool(i & 0b0000_0100),
        bool(i & 0b0000_1000),
        bool(i & 0b0001_0000),
        bool(i & 0b0010_0000),
        bool(i & 0b0100_0000),
        bool(i & 0b1000_0000)
    )
    for i in range(256)
}
