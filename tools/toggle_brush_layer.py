import bpy
from ..setup_tools.register import register_wrap



def _ToggleBrushLayer(context, name_pen='', name_layer='', 
                        gpencil_color_mode='MATERIAL'):
    """ Arguments
        name_pen: str, name of the brush you wanna use.
        name_layer: str, name of the layer you wanna draw on
        gpencil_color_mode: str, 'MATERIAL' or 'VERTEXCOLOR'
    """                            
    # context.active_object.data.layers.active.lock=True
    bpy.ops.gpencil.lock_all()

    
    current_GPen = context.active_object.data
    
    
    context.tool_settings.gpencil_paint.brush = bpy.data.brushes[name_pen]
    current_GPen.layers.active = current_GPen.layers[name_layer]
    context.scene.tool_settings.gpencil_paint.color_mode = gpencil_color_mode
    
    context.active_object.data.layers.active.lock = False




@register_wrap
class MYBLENDRC_OT_GPencilToggleBrush_1(bpy.types.Operator):
    """change to Blue draft brush"""
    bl_idname = "myblendrc.gpen_to_slot1"
    bl_label = "1"
    bl_description = "1 change grease pencil brush and layer to Blue draft"
    
    def execute(self, context):        
        _ToggleBrushLayer(context, 
                                  name_pen='1gp',
                                name_layer='draft_1',
                        gpencil_color_mode='MATERIAL')                            
        
        return {'FINISHED'}  


@register_wrap
class MYBLENDRC_OT_GPencilToggleBrush_2(bpy.types.Operator):
    """change to Green draft brush"""
    bl_idname = "myblendrc.gpen_to_slot2"
    bl_label = "2"
    bl_description = "2 change grease pencil brush and layer to Green draft"
    
    def execute(self, context):
        _ToggleBrushLayer(context, 
                                  name_pen='2gp',
                                name_layer='draft_2',
                        gpencil_color_mode='MATERIAL')                            
        
        return {'FINISHED'}    

    
@register_wrap
class MYBLENDRC_OT_GPencilToggleBrush_3(bpy.types.Operator):
    """change to Red draft brush"""
    bl_idname = "myblendrc.gpen_to_slot3"
    bl_label = "3"
    bl_description = "3 change grease pencil brush and layer to Red draft"
    
    def execute(self, context):
        _ToggleBrushLayer(context, 
                                  name_pen='3gp',
                                name_layer='draft_3',
                        gpencil_color_mode='MATERIAL')                            
    
        return {'FINISHED'}
    


@register_wrap
class MYBLENDRC_OT_GPencilToggleBrush_4(bpy.types.Operator):
    """change to tight line brush"""
    bl_idname = "myblendrc.gpen_to_slot4"
    bl_label = "4"
    bl_description = "4 change grease pencil brush and layer to Tight line"
    
    def execute(self, context):
        _ToggleBrushLayer(context, 
                                  name_pen='4gp',
                                name_layer='line',
                        gpencil_color_mode='MATERIAL')                            
    
        return {'FINISHED'}



@register_wrap
class MYBLENDRC_OT_GPencilToggleBrush_5(bpy.types.Operator):
    """change to shade fill brush"""
    bl_idname = "myblendrc.gpen_to_slot5"
    bl_label = "5"
    bl_description = "5 change grease pencil brush and layer to Shade Fill"
    
    def execute(self, context):
        _ToggleBrushLayer(context, 
                                  name_pen='5gp',
                                name_layer='fill',
                        gpencil_color_mode='VERTEXCOLOR')
                                
        return {'FINISHED'}
    
    
    

