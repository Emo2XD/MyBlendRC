import bpy
from ..setup_tools.register import register_wrap


@register_wrap
class MYBLENDRC_MT_Q_MENU(bpy.types.Menu):
    bl_label = "Custom Q Menu"
    bl_idname = "myblendrc.q_menu"

    def draw(self, context):
        layout = self.layout

        layout.menu("SCREEN_MT_user_menu", text="Q Quick Favorites")

        layout.separator()
        layout.operator("myblendrc.toggle_mesh_visibility")
        layout.operator("myblendrc.toggle_gpencil_visibility")
