import bpy
import os
from pathlib import Path
from ..setup_tools.register import register_wrap

@register_wrap
class MYBLENDRC_OT_GPencilSetupLayers(bpy.types.Operator):
    """ Set up layers for brush toggle functions. """
    bl_idname = "myblendrc.gpencil_setup_layers"
    bl_label = "Setup Layers For Toggle Funcsions"
    # bl_description = "Force add new keyframe on all layers even on locked ones"
    
    def execute(self, context):        
        self.__add_new_layer("fill")
        self.__add_new_layer("draft_1")
        self.__add_new_layer("draft_2")
        self.__add_new_layer("draft_3")
        self.__add_new_layer("line")

        # Disable use lights option for layers.
        for l in context.object.data.layers:
            l.use_lights = False

        return {'FINISHED'}  

    
    def __add_new_layer(self, name="new_layer"):
        '''add new layer but do not override existing same name layer.'''
        
        if name in [l_name.info for l_name in bpy.context.object.data.layers]:
            print(f'Layer named \'{name}\' already exists, no override.')        
        else:
            bpy.context.object.data.layers.new(name, set_active=True)
            print(f'Layer named \'{name}\' was successfully created.')        
            pass




@register_wrap
class MYBLENDRC_OT_GPencilBrushSetup(bpy.types.Operator):
    """ Set up brushes for brush toggle functions. """
    bl_idname = "myblendrc.gpencil_setup_brushes"
    bl_label = "Setup Brushes For Toggle Funcsions"
    # bl_description = "Force add new keyframe on all layers even on locked ones"
    
    def execute(self, context):        
        # Grease pencil brush
        self.__append_brush('1gp')
        self.__append_brush('2gp')
        self.__append_brush('3gp')
        self.__append_brush('4gp')
        self.__append_brush('5gp')
        # Grease pencil eraser
        self.__append_brush('1gpe')
        self.__append_brush('2gpe')
        self.__append_brush('3gpe')
        self.__append_brush('4gpe')

        return {'FINISHED'}  

    def __append_brush(self, name=''):
        ''' Append a brush from external file, but no override when there is
            a same brush.
        '''
        this_file_path = Path(__file__)
        
        file_path = str(this_file_path.parent.parent / 'blender_files/brushes_export.blend')
        inner_path = 'Brush'
        object_name = name
        
        if name in [b.name for b in bpy.data.brushes]:
            print(f"Brush \'{name}\' already exists, no override.")
            
        else:
            bpy.ops.wm.append(
            filepath=os.path.join(file_path, inner_path, object_name),
            directory=os.path.join(file_path, inner_path),
            filename=object_name
            )
            print(f"Brush \'{name}\' was successfully appended.")
