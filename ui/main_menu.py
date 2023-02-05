import bpy
from ..setup_tools.register import register_wrap


@register_wrap
class MYBLENDRC_MT_MAIN_MENU(bpy.types.Menu):
    bl_label = "Custom Main Menu"
    bl_idname = "myblendrc.main_menu"

    def draw(self, context):
        layout = self.layout

        if context.object.type == 'GPENCIL':
            layout.operator("myblendrc.gpen_to_slot1")
            layout.operator("myblendrc.gpen_to_slot2")
            layout.operator("myblendrc.gpen_to_slot3")
            layout.operator("myblendrc.gpen_to_slot4")
            layout.operator("myblendrc.gpen_to_slot5")

            layout.separator()

            layout.operator("myblendrc.gpencil_force_frame_add_all")
            layout.operator("gpencil.lock_all", text="L lock all layers")
            layout.operator("gpencil.unlock_all", text="U unlock all layers")
         
        layout.separator()
        layout.operator("myblendrc.toggle_mesh_visibility")
