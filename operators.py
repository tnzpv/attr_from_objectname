import bpy
from . import functions


class DrawtypeOperator(bpy.types.Operator):
    bl_idname = "scene.drawtype_from_objects"
    bl_label = "Drawtype from Objects Names"
    bl_description = "Change Max drawtype from Objects names"

    draw_type = bpy.props.StringProperty(name='drawtype')

    def execute(self, context):
        functions.change_max_drawtype(self.draw_type)
        return {'FINISHED'}


class ShowHideOperator(bpy.types.Operator):
    bl_idname = "scene.show_hide"
    bl_label = "Show/Hide from Objects Names"
    bl_description = "Show/Hide from Objects Names"

    hide = bpy.props.BoolProperty(name='hide')

    def execute(self, context):
        functions.showhide(self.hide)
        return {'FINISHED'}


class ShowHideOthersOperator(bpy.types.Operator):
    bl_idname = "scene.show_hide_others"
    bl_label = "Show/Hide others from Objects Names"
    bl_description = "Show/Hide others from Objects Names"

    hide = bpy.props.BoolProperty(name='hide')

    def execute(self, context):
        functions.showhide(self.hide, others=True)
        return {'FINISHED'}
