if "bpy" not in locals():
    import bpy
    from . import register
else:
    import importlib
    importlib.reload(register)
