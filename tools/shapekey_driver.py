# Create Shapekey driver.
# This will apply driver to change the shapekey value
# that shares the same name


import bpy
from ..setup_tools.register import register_wrap

# bpy.data.shape_keys['Key.003'].key_blocks['Key 2'].value <- this data will have a driver

def shape_key_link_add_driver(
        driverToBeCreated, driverVar):
    ''' Add driver to target '''
    
    d = driverToBeCreated.driver_add('value').driver
    
    v = d.variables.new() # create variable
    v.name = 'value' # variable name
    v.targets[0].id_type = 'KEY'

    v.targets[0].id = driverVar.id_data # kind Key.001
    
    
    v.targets[0].data_path = "key_blocks[\"{}\"].value".format(driverToBeCreated.name)
    
    
    d.expression = v.name





class ParseSelectedObjects:
    def __init__(self):
        ''' Parse non active and active object '''
        self.active = bpy.context.active_object        
        
        selected = bpy.context.selected_objects
        selected.remove(self.active)
        
        self.non_active = selected


            
def GetShapeKey(object):
    return object.active_shape_key.id_data
    



@register_wrap
class MYBLENDRC_OT_ShapeKeyDriver(bpy.types.Operator):
    """ Apply driver to change the shapekey value that shares the same name at once"""
    bl_idname = "myblendrc.shapkey_driver"
    bl_label = "Add ShapeKey Driver"
    bl_description = "Add ShapeKey driver that shares the same shapekey name"
            
    
    def execute(self, context):

        selected = ParseSelectedObjects()


        driverToBeCreated_objects = selected.non_active # non active object
        driverVar_object = selected.active # active object

        # retrieve any related Key (kind bpy.data.shape_keys["Key.003"] <- contains several similar kind of data in Keys)
        driverToBeCreated_Keys = [GetShapeKey(key) for key in driverToBeCreated_objects]
        driverVar_Key = GetShapeKey(driverVar_object) # only one Key (not blocks)


        # apply driver
        for shape_keys in driverToBeCreated_Keys:
            for driverToBeCreated in shape_keys.key_blocks:
                
                #kind shape_keys['Key.003'].key_blocks['Key 2'] # select same name key_blocks
                driverVar = driverVar_Key.key_blocks[driverToBeCreated.name]
                
                shape_key_link_add_driver(driverToBeCreated,  driverVar)

        return {'FINISHED'}
