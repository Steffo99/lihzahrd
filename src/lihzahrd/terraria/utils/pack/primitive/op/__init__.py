# language=rst
"""
Module containing mixins to add various operators to classes inheriting from :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive`.

.. admonition:: Example

    To allow instances of a class inheriting from :class:`~lihzahrd.terraria.utils.pack.primitive.int.PackInt` to behave like regular :class:`int` would, you can mixin :class:`~lihzahrd.terraria.utils.pack.primitive.op.integer.OpInteger`::

        class WorldRevision(OpInteger, PackInt):
            ...

    Allowing for code like the following::

        p1: WorldRevision = WorldRevision.read(fp).instance
        p2: WorldRevision = WorldRevision.read(fp).instance
        p3: WorldRevision = p1 + p2
        assert p3.value == p1.value + p2.value


``equality``
------------

.. automodule:: lihzahrd.terraria.utils.pack.primitive.op.equality
    :undoc-members:
    :exclude-members: value
    :special-members: __eq__, __ne__


``boolean``
-----------

.. automodule:: lihzahrd.terraria.utils.pack.primitive.op.boolean
    :undoc-members:
    :exclude-members: value
    :special-members: __bool__, __and__, __iand__, __or__, __ior__, __xor__, __ixor__, __invert__


``collection``
--------------

.. automodule:: lihzahrd.terraria.utils.pack.primitive.op.collection
    :undoc-members:
    :exclude-members: value
    :special-members: __len__, __length_hint__, __getitem__, __setitem__, __delitem__, __iter__, __reversed__, __contains__


``comparison``
--------------

.. automodule:: lihzahrd.terraria.utils.pack.primitive.op.comparison
    :undoc-members:
    :exclude-members: value
    :special-members: __gt__, __ge__, __lt__, __le__


``number``
----------

.. automodule:: lihzahrd.terraria.utils.pack.primitive.op.number
    :undoc-members:
    :exclude-members: value
    :special-members: __neg__, __pos__, __abs__, __add__, __iadd__, __sub__, __isub__, __mul__, __imul__, __truediv__, __itruediv__


``integer``
-----------

.. automodule:: lihzahrd.terraria.utils.pack.primitive.op.integer
    :undoc-members:
    :exclude-members: value
    :special-members: __int__, __index__, __floordiv__, __ifloordiv__, __mod__, __imod__, __lshift__, __ilshift__, __rshift__, __irshift__


``floating``
------------

.. automodule:: lihzahrd.terraria.utils.pack.primitive.op.floating
    :undoc-members:
    :exclude-members: value
    :special-members: __float__, __complex__, __round__, __trunc__, __floor__,__ceil__

"""
