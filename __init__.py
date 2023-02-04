bl_info = {
    'name': 'MyBlendRC',
    'category': '3D View',
    'author': 'Emo2XD',
    'location': 'Access by pressing spacebar or Q in 3D view',
    'description': 'Extending menu function in Blender.',
    'version': (0, 0, 1),  # Has to be (x, x, x) not [x, x, x]!! Only change this version and the dev branch var right before publishing the new update!
    'blender': (2, 80, 0),
    'wiki_url': '',
    'tracker_url': '',
    'warning': '',
}

from .key_mapping import keymap

if "bpy" not in locals():
    import bpy
    from . import setup_tools
    from . import tools
    from . import ui

else:
    import importlib
    importlib.reload(setup_tools)
    importlib.reload(tools)
    importlib.reload(ui)


addon_keymaps=[]

def register():
    for cls in setup_tools.register.__bl_classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', ctrl=False, shift=False, alt=False)
        kmi.properties.name =  ui.main_menu.MYBLENDRC_MT_MAIN_MENU.bl_idname
        addon_keymaps.append((km, kmi))
        
        kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', ctrl=False, shift=False, alt=False)
        kmi.properties.name = ui.q_menu.MYBLENDRC_MT_Q_MENU.bl_idname
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in setup_tools.register.__bl_classes:
        bpy.utils.unregister_class(cls)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == '__main__':
    register()
