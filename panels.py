import bpy

class AttrObjectNamePanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Animation'
    bl_label = "Attributes from Objects Names"

    def draw(self, context):
        row = self.layout.row()
        row.prop(context.scene, 'attr_regex', text='Regex')

        layout = self.layout.column(align=True)
        row = layout.row(align=True)
        row.operator('scene.show_hide', text='Show', icon='VISIBLE_IPO_ON').hide = False
        row.operator('scene.show_hide', text='Hide', icon='VISIBLE_IPO_OFF').hide = True
        row = layout.row(align=True)
        row.operator(
            'scene.show_hide_others',
            text='Show others',
            icon='VISIBLE_IPO_ON').hide = False
        row.operator(
            'scene.show_hide_others',
            text='Hide others',
            icon='VISIBLE_IPO_OFF').hide = True

        layout = self.layout.column(align=True)
        for index, drawtype in enumerate(('BOUNDS', 'WIRE', 'SOLID', 'TEXTURED')):
            if index%2 == 0:
                row = layout.row(align=True)
            row.operator('scene.drawtype_from_objects', text=drawtype.title()).draw_type = drawtype
