'''
	*** Begin GPL License Block ***

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>
	or write to the Free Software Foundation,
	Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

	*** End GPL License Block ***
'''
''' (c)2018 GameSolids '''

''' UI Panel layout for Billboard Resource Creator '''
import bpy, os, logging
from bpy.props import FloatVectorProperty, StringProperty, BoolProperty, PointerProperty

class VIEW3D_PT_billboard_resources_panel(bpy.types.Panel):
	''' UI Panel for creating billboard assets '''
	bl_idname = "view3d.billboard_resources_panel"
	bl_label = "Billboard Resources"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = "View"
	bl_context = 'objectmode'
	
	def draw(self, context):
		''' display logic and layout '''
		##TODO: make this more friendly
		scene = context.scene               
		layout = self.layout

		layout.prop_search(scene.gs_template, "billboard_object", scene, "objects")
		layout.prop_search(scene.gs_template, "billboard_cage", scene, "objects")

		row = layout.row()
		
		row.operator("gs_billboard.setup_template_button")
		row.operator("gs_billboard.clear_template_button")

		layout.label(text="Texture Export Options")
		layout.prop(scene.gs_settings, "filename")

		row = layout.row()
		row.prop(scene.gs_settings, "combined")
		row.prop(scene.gs_settings, "combined_sfx")

		row = layout.row()
		row.prop(scene.gs_settings, "diffuse")
		row.prop(scene.gs_settings, "diffuse_sfx")

		row = layout.row()
		row.prop(scene.gs_settings, "normal")
		row.prop(scene.gs_settings, "normal_sfx")

		row = layout.row()
		row.prop(scene.gs_settings, "ambio")
		row.prop(scene.gs_settings, "ambio_sfx")

		layout.prop(scene.gs_settings, "unityComponent")
		#layout.prop(scene.gs_settings, "unrealComponent")

		layout.prop(scene, "gs_billboard_path")
		layout.operator("gs_billboard.render_atlas_button", text="Export Package")


