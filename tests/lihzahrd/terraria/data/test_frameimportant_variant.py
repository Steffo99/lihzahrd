from lihzahrd.terraria.data.frameimportant_variant import FrameImportantVariant


def test_evaluate_empty():
    fiv = FrameImportantVariant()
    assert fiv.evaluate()
    assert fiv.evaluate(u=6)
    assert fiv.evaluate(v=7)
    assert fiv.evaluate(u=6, v=7)


def test_evaluate_eq_u():
    fiv = FrameImportantVariant(eq_u=1)
    assert fiv.evaluate(u=1)
    assert fiv.evaluate(u=1, v=2)
    assert not fiv.evaluate(u=2)
    assert not fiv.evaluate()
    assert not fiv.evaluate(v=1)


def test_evaluate_eq_v():
    fiv = FrameImportantVariant(eq_v=2)
    assert fiv.evaluate(v=2)
    assert fiv.evaluate(u=1, v=2)
    assert not fiv.evaluate(u=2)
    assert not fiv.evaluate()
    assert not fiv.evaluate(v=1)


def test_evaluate_eq_uv():
    fiv = FrameImportantVariant(eq_u=1, eq_v=2)
    assert fiv.evaluate(u=1, v=2)
    assert not fiv.evaluate(u=2, v=2)
    assert not fiv.evaluate(u=1, v=1)
    assert not fiv.evaluate()
    assert not fiv.evaluate(u=1)
    assert not fiv.evaluate(v=2)
    assert not fiv.evaluate(u=2, v=3)


def test_evaluate_min_u():
    fiv = FrameImportantVariant(min_u=1)
    assert fiv.evaluate(u=1)
    assert fiv.evaluate(u=2)
    assert fiv.evaluate(u=3)
    assert fiv.evaluate(u=2, v=0)
    assert not fiv.evaluate(u=0)
    assert not fiv.evaluate()
    assert not fiv.evaluate(v=1)
    assert not fiv.evaluate(v=2)


def test_evaluate_min_v():
    fiv = FrameImportantVariant(min_v=1)
    assert fiv.evaluate(v=1)
    assert fiv.evaluate(v=2)
    assert fiv.evaluate(v=3)
    assert fiv.evaluate(u=0, v=2)
    assert not fiv.evaluate(v=0)
    assert not fiv.evaluate()
    assert not fiv.evaluate(u=1)
    assert not fiv.evaluate(u=2)


def test_evaluate_max_u():
    fiv = FrameImportantVariant(max_u=1)
    assert fiv.evaluate(u=0)
    assert fiv.evaluate(u=1)
    assert fiv.evaluate(u=0, v=2)
    assert not fiv.evaluate(u=2)
    assert not fiv.evaluate(u=3)
    assert not fiv.evaluate()
    assert not fiv.evaluate(v=1)
    assert not fiv.evaluate(v=2)


def test_evaluate_max_v():
    fiv = FrameImportantVariant(max_v=1)
    assert fiv.evaluate(v=0)
    assert fiv.evaluate(v=1)
    assert fiv.evaluate(u=2, v=0)
    assert not fiv.evaluate(v=2)
    assert not fiv.evaluate(v=3)
    assert not fiv.evaluate()
    assert not fiv.evaluate(u=1)
    assert not fiv.evaluate(u=2)


def test_evaluate_minmax_uv():
    fiv = FrameImportantVariant(min_u=10, max_u=20, min_v=30, max_v=40)
    assert fiv.evaluate(u=15, v=35)
    assert fiv.evaluate(u=10, v=30)
    assert fiv.evaluate(u=20, v=40)
    assert not fiv.evaluate()
    assert not fiv.evaluate(u=10)
    assert not fiv.evaluate(u=15)
    assert not fiv.evaluate(u=20)
    assert not fiv.evaluate(v=30)
    assert not fiv.evaluate(v=35)
    assert not fiv.evaluate(v=40)
    assert not fiv.evaluate(u=15, v=15)
    assert not fiv.evaluate(u=35, v=35)
    assert not fiv.evaluate(u=0, v=0)
