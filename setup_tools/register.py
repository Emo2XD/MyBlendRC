import bpy

__bl_classes = []

def register_wrap(cls):
    __bl_classes.append(cls)
    return cls