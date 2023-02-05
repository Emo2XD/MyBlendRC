import bpy
from ..setup_tools.register import register_wrap


@register_wrap
class MYBLENDRC_OT_GPencilForceFrameAddAll(bpy.types.Operator):
    """change to Blue draft brush"""
    bl_idname = "myblendrc.gpencil_force_frame_add_all"
    bl_label = "I Force Add Frame All layers "
    bl_description = "Force add new keyframe on all layers even on locked ones"
    
    def execute(self, context):        
        
        bpy.ops.gpencil.unlock_all()
        bpy.ops.gpencil.blank_frame_add(all_layers=True)
        bpy.ops.gpencil.lock_all()
        context.active_object.data.layers.active.lock = False
        return {'FINISHED'}  

