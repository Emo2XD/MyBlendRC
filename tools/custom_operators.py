import bpy
from ..setup_tools.register import register_wrap

@register_wrap
class MYBLENDRC_OT_CameraFlip(bpy.types.Operator):
    """ Flip camera scale X """
    bl_idname = "myblendrc.camera_flip"
    bl_label = "F Flip Camera Scale X"
    # bl_description = "Flip camera scale X"
    
    def execute(self, context):        
        camera = context.scene.camera
        camera.scale[0] *= -1
        return {'FINISHED'}  




@register_wrap
class MYBLENDRC_OT_PaintThrough(bpy.types.Operator):
    """Toggle brush settings at once, including normal falloff, occlude and backface culling"""
    bl_idname = "myblendrc.toggle_paint_through"
    bl_label = "T Paint Through Toggle"
            
    
    def execute(self, context):
        # get current texture paint state by normal falloff property
        current_state = context.scene.tool_settings.image_paint.use_normal_falloff
        # Your code here ...
        if current_state == False:
            context.scene.tool_settings.image_paint.use_normal_falloff   = True
            context.scene.tool_settings.image_paint.use_occlude          = True
            context.scene.tool_settings.image_paint.use_backface_culling = True
           
        else:
            context.scene.tool_settings.image_paint.use_normal_falloff   = False
            context.scene.tool_settings.image_paint.use_occlude          = False
            context.scene.tool_settings.image_paint.use_backface_culling = False
                  
        
        return {'FINISHED'}

@register_wrap
class MYBLENDRC_OT_ToggleStrokeMethod(bpy.types.Operator):
    """Toggle brush stroke method between 'Space' and 'Line'"""
    bl_idname = "myblendrc.toggle_stroke_method"
    bl_label = "S Stroke Method Toggle"
    
    def execute(self, context):
        current_stroke_method = context.tool_settings.image_paint.brush.stroke_method
        
        if current_stroke_method == 'SPACE':
            context.tool_settings.image_paint.brush.stroke_method = 'LINE'
        elif current_stroke_method == 'LINE':
            context.tool_settings.image_paint.brush.stroke_method = 'SPACE'
        else:
            context.tool_settings.image_paint.brush.stroke_method = 'SPACE'
        
        return {'FINISHED'}
# @register_wrap
# class MYBLENDRC_OT_LockCameraToView(bpy.types.Operator):
#     """ Lock camera to view. """
#     bl_idname = "myblendrc.lock_camera_to_veiw"
#     bl_label = "L Lock Camera To View"
#     # bl_description = "Flip camera scale X"
    
#     def execute(self, context):        
#         camera = context.scene.camera
#         camera.scale[0] *= -1
#         return {'FINISHED'}  
