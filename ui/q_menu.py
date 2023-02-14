import bpy
from ..setup_tools.register import register_wrap


@register_wrap
class MYBLENDRC_MT_Q_MENU(bpy.types.Menu):
    bl_label = "Custom Q Menu"
    bl_idname = "myblendrc.q_menu"

    def draw(self, context):
        
        layout = self.layout

        # view = context.space_data
        # layout.prop(view, "lock_camera", text="L Lock Camera")

        layout.menu("SCREEN_MT_user_menu", text="Q Quick Favorites")

        layout.separator()
        layout.operator("myblendrc.toggle_mesh_visibility")
        layout.operator("myblendrc.toggle_gpencil_visibility")
        layout.operator("myblendrc.camera_flip")
        
        # Edit mode menu
        if context.object.type == 'MESH':
            if context.active_object.mode=='EDIT':
                if context.tool_settings.mesh_select_mode[1] == 1:# edge selection mode
                    layout.operator("mesh.mark_sharp", text="H Clear Sharp").clear = True
                    layout.operator("mesh.mark_seam", text="M Clear Seam").clear = True
        # layout.operator("SpaceView3D.lock_camera")
        
            elif context.active_object.mode=='TEXTURE_PAINT':
                layout.operator("myblendrc.toggle_paint_through")
                layout.operator("myblendrc.toggle_stroke_method")
        

        # elif context.object.type == 'GPENCIL':
        #     layout.operator("gpencil.hide", text="H Hide Other Layers").unselected = True

        #     layout.operator("gpencil.reveal", text="Z Reveal All Layers")



