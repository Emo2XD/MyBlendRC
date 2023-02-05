import bpy
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
