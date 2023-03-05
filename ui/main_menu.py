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
            layout.operator("myblendrc.gpen_eraser_to_slot3", text="E change brush to \'3gpe\'")

            layout.separator()
            layout.operator("myblendrc.gpencil_force_frame_add_all")
            layout.operator("gpencil.lock_all", text="L lock all layers")
            layout.operator("gpencil.unlock_all", text="U unlock all layers")

        # elif context.object.type == 'MESH':
        #     if context.active_object.mode=='TEXTURE_PAINT':
        #         layout.operator("myblendrc.toggle_paint_through")
        #         layout.operator("myblendrc.toggle_stroke_method")

         
        layout.separator()
        layout.operator("myblendrc.camera_flip")
        layout.operator("myblendrc.toggle_mesh_visibility")

