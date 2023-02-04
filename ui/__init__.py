if "bpy" not in locals():
    import bpy
    from . import gpencil_submenu 
    from . import main_menu
    from . import q_menu
else:
    import importlib
    importlib.reload(gpencil_submenu)
    importlib.reload(main_menu)
    importlib.reload(q_menu)
