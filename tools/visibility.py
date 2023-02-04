import bpy
from ..setup_tools.register import register_wrap

@register_wrap
class MYBLENDRC_OT_MeshVisibility(bpy.types.Operator):
    """Hide / unhide mesh"""
    bl_idname = "myblendrc.toggle_mesh_visibility"
    bl_label = "W Toggle Mesh Visibility"
    bl_description = "Toggles mesh visibility for grease pencil drawing."
            
    
    def execute(self, context):
        current_state = context.space_data.show_object_viewport_mesh
        # Your code here ...
        if current_state == True:
            context.space_data.show_object_viewport_mesh = False
        else:
            context.space_data.show_object_viewport_mesh = True
        
    
        return {'FINISHED'}

@register_wrap
class MYBLENDRC_OT_GPencilVisibility(bpy.types.Operator):
    """Hide / unhide grease pencil"""
    bl_idname = "myblendrc.toggle_gpencil_visibility"
    bl_label = "G Toggle Grease Pencil Visibility"
    bl_description = "Toggles grease pencil visibility for modeling."
            
    
    def execute(self, context):
        current_state = context.space_data.show_object_viewport_grease_pencil
        # context.space_data.show_object_viewport_grease_pencil != current_state

        # Your code here ...
        if current_state == True:
            context.space_data.show_object_viewport_grease_pencil = False
        else:
            # context.space_data.show_object_viewport_mesh = True
            context.space_data.show_object_viewport_grease_pencil = True
        
    
        return {'FINISHED'}
