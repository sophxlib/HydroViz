# trace generated using paraview version 5.10.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'NetCDF Reader'
iDA_2021_0829_all_data_c29nc = NetCDFReader(registrationName='IDA_2021_08-29_all_data_c29.nc', FileName=['/Users/sophiahu/HurricaneVis/IDA_2021_08-29_all_data_c29.nc'])
iDA_2021_0829_all_data_c29nc.Dimensions = '(Scanline, Field_of_view, Channel)'

# create a new 'NetCDF Reader'
iDA_2021_0829_all_data_c29nc_1 = NetCDFReader(registrationName='IDA_2021_08-29_all_data_c29.nc', FileName=['/Users/sophiahu/HurricaneVis/IDA_2021_08-29_all_data_c29.nc'])
iDA_2021_0829_all_data_c29nc_1.Dimensions = '(Scanline, Field_of_view, Channel)'

# create a new 'NetCDF Reader'
iDA_2021_0829_all_data_c29nc_2 = NetCDFReader(registrationName='IDA_2021_08-29_all_data_c29.nc', FileName=['/Users/sophiahu/HurricaneVis/IDA_2021_08-29_all_data_c29.nc'])
iDA_2021_0829_all_data_c29nc_2.Dimensions = '(Scanline, Field_of_view, Channel)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
iDA_2021_0829_all_data_c29nc_1Display = Show(iDA_2021_0829_all_data_c29nc_1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
iDA_2021_0829_all_data_c29nc_1Display.Representation = 'Outline'
iDA_2021_0829_all_data_c29nc_1Display.ColorArrayName = [None, '']
iDA_2021_0829_all_data_c29nc_1Display.SelectTCoordArray = 'None'
iDA_2021_0829_all_data_c29nc_1Display.SelectNormalArray = 'None'
iDA_2021_0829_all_data_c29nc_1Display.SelectTangentArray = 'None'
iDA_2021_0829_all_data_c29nc_1Display.OSPRayScaleArray = 'BT'
iDA_2021_0829_all_data_c29nc_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29nc_1Display.SelectOrientationVectors = 'None'
iDA_2021_0829_all_data_c29nc_1Display.ScaleFactor = 21.5
iDA_2021_0829_all_data_c29nc_1Display.SelectScaleArray = 'BT'
iDA_2021_0829_all_data_c29nc_1Display.GlyphType = 'Arrow'
iDA_2021_0829_all_data_c29nc_1Display.GlyphTableIndexArray = 'BT'
iDA_2021_0829_all_data_c29nc_1Display.GaussianRadius = 1.075
iDA_2021_0829_all_data_c29nc_1Display.SetScaleArray = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29nc_1Display.ScaleTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29nc_1Display.OpacityArray = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29nc_1Display.OpacityTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29nc_1Display.DataAxesGrid = 'GridAxesRepresentation'
iDA_2021_0829_all_data_c29nc_1Display.PolarAxes = 'PolarAxesRepresentation'
iDA_2021_0829_all_data_c29nc_1Display.ScalarOpacityUnitDistance = 3.1291908726725213
iDA_2021_0829_all_data_c29nc_1Display.OpacityArrayName = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29nc_1Display.SliceFunction = 'Plane'
iDA_2021_0829_all_data_c29nc_1Display.Slice = 107

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
iDA_2021_0829_all_data_c29nc_1Display.ScaleTransferFunction.Points = [129.6, 0.0, 0.5, 0.0, 290.58, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
iDA_2021_0829_all_data_c29nc_1Display.OpacityTransferFunction.Points = [129.6, 0.0, 0.5, 0.0, 290.58, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
iDA_2021_0829_all_data_c29nc_1Display.SliceFunction.Origin = [10.5, 47.5, 107.5]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show data in view
iDA_2021_0829_all_data_c29nc_2Display = Show(iDA_2021_0829_all_data_c29nc_2, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
iDA_2021_0829_all_data_c29nc_2Display.Representation = 'Outline'
iDA_2021_0829_all_data_c29nc_2Display.ColorArrayName = [None, '']
iDA_2021_0829_all_data_c29nc_2Display.SelectTCoordArray = 'None'
iDA_2021_0829_all_data_c29nc_2Display.SelectNormalArray = 'None'
iDA_2021_0829_all_data_c29nc_2Display.SelectTangentArray = 'None'
iDA_2021_0829_all_data_c29nc_2Display.OSPRayScaleArray = 'BT'
iDA_2021_0829_all_data_c29nc_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29nc_2Display.SelectOrientationVectors = 'None'
iDA_2021_0829_all_data_c29nc_2Display.ScaleFactor = 21.5
iDA_2021_0829_all_data_c29nc_2Display.SelectScaleArray = 'BT'
iDA_2021_0829_all_data_c29nc_2Display.GlyphType = 'Arrow'
iDA_2021_0829_all_data_c29nc_2Display.GlyphTableIndexArray = 'BT'
iDA_2021_0829_all_data_c29nc_2Display.GaussianRadius = 1.075
iDA_2021_0829_all_data_c29nc_2Display.SetScaleArray = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29nc_2Display.ScaleTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29nc_2Display.OpacityArray = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29nc_2Display.OpacityTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29nc_2Display.DataAxesGrid = 'GridAxesRepresentation'
iDA_2021_0829_all_data_c29nc_2Display.PolarAxes = 'PolarAxesRepresentation'
iDA_2021_0829_all_data_c29nc_2Display.ScalarOpacityUnitDistance = 3.1291908726725213
iDA_2021_0829_all_data_c29nc_2Display.OpacityArrayName = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29nc_2Display.SliceFunction = 'Plane'
iDA_2021_0829_all_data_c29nc_2Display.Slice = 107

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
iDA_2021_0829_all_data_c29nc_2Display.ScaleTransferFunction.Points = [129.6, 0.0, 0.5, 0.0, 290.58, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
iDA_2021_0829_all_data_c29nc_2Display.OpacityTransferFunction.Points = [129.6, 0.0, 0.5, 0.0, 290.58, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
iDA_2021_0829_all_data_c29nc_2Display.SliceFunction.Origin = [10.5, 47.5, 107.5]

# show data in view
iDA_2021_0829_all_data_c29ncDisplay = Show(iDA_2021_0829_all_data_c29nc, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
iDA_2021_0829_all_data_c29ncDisplay.Representation = 'Outline'
iDA_2021_0829_all_data_c29ncDisplay.ColorArrayName = [None, '']
iDA_2021_0829_all_data_c29ncDisplay.SelectTCoordArray = 'None'
iDA_2021_0829_all_data_c29ncDisplay.SelectNormalArray = 'None'
iDA_2021_0829_all_data_c29ncDisplay.SelectTangentArray = 'None'
iDA_2021_0829_all_data_c29ncDisplay.OSPRayScaleArray = 'BT'
iDA_2021_0829_all_data_c29ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29ncDisplay.SelectOrientationVectors = 'None'
iDA_2021_0829_all_data_c29ncDisplay.ScaleFactor = 21.5
iDA_2021_0829_all_data_c29ncDisplay.SelectScaleArray = 'BT'
iDA_2021_0829_all_data_c29ncDisplay.GlyphType = 'Arrow'
iDA_2021_0829_all_data_c29ncDisplay.GlyphTableIndexArray = 'BT'
iDA_2021_0829_all_data_c29ncDisplay.GaussianRadius = 1.075
iDA_2021_0829_all_data_c29ncDisplay.SetScaleArray = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29ncDisplay.OpacityArray = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data_c29ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
iDA_2021_0829_all_data_c29ncDisplay.PolarAxes = 'PolarAxesRepresentation'
iDA_2021_0829_all_data_c29ncDisplay.ScalarOpacityUnitDistance = 3.1291908726725213
iDA_2021_0829_all_data_c29ncDisplay.OpacityArrayName = ['POINTS', 'BT']
iDA_2021_0829_all_data_c29ncDisplay.SliceFunction = 'Plane'
iDA_2021_0829_all_data_c29ncDisplay.Slice = 107

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
iDA_2021_0829_all_data_c29ncDisplay.ScaleTransferFunction.Points = [129.6, 0.0, 0.5, 0.0, 290.58, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
iDA_2021_0829_all_data_c29ncDisplay.OpacityTransferFunction.Points = [129.6, 0.0, 0.5, 0.0, 290.58, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
iDA_2021_0829_all_data_c29ncDisplay.SliceFunction.Origin = [10.5, 47.5, 107.5]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# Properties modified on iDA_2021_0829_all_data_c29nc
iDA_2021_0829_all_data_c29nc.Dimensions = '(Scanline, Field_of_view)'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.Slice = 0

# set scalar coloring
ColorBy(iDA_2021_0829_all_data_c29ncDisplay, ('POINTS', 'RR'))

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data_c29ncDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data_c29ncDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'RR'
rRLUT = GetColorTransferFunction('RR')

# get opacity transfer function/opacity map for 'RR'
rRPWF = GetOpacityTransferFunction('RR')

# change representation type
iDA_2021_0829_all_data_c29ncDisplay.SetRepresentationType('Slice')

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# Properties modified on iDA_2021_0829_all_data_c29nc_1
iDA_2021_0829_all_data_c29nc_1.Dimensions = '(Scanline, Field_of_view, P_Layer)'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(iDA_2021_0829_all_data_c29nc_1Display, ('POINTS', 'PTemp'))

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data_c29nc_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data_c29nc_1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'PTemp'
pTempLUT = GetColorTransferFunction('PTemp')

# get opacity transfer function/opacity map for 'PTemp'
pTempPWF = GetOpacityTransferFunction('PTemp')

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# Properties modified on iDA_2021_0829_all_data_c29nc_2
iDA_2021_0829_all_data_c29nc_2.Dimensions = '(Scanline, Field_of_view, P_Layer)'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(iDA_2021_0829_all_data_c29nc_2Display, ('POINTS', 'PTemp'))

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data_c29nc_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data_c29nc_2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=iDA_2021_0829_all_data_c29nc_1)
contour1.ContourBy = ['POINTS', 'PClw']
contour1.Isosurfaces = [0.03952397406795624]
contour1.PointMergeMethod = 'Uniform Binning'

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'PClw'
pClwLUT = GetColorTransferFunction('PClw')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'PClw']
contour1Display.LookupTable = pClwLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'PClw'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 20.319801139831544
contour1Display.SelectScaleArray = 'PClw'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'PClw'
contour1Display.GaussianRadius = 1.0159900569915772
contour1Display.SetScaleArray = ['POINTS', 'PClw']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'PClw']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.03952397406101227, 0.0, 0.5, 0.0, 0.03953160345554352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.03952397406101227, 0.0, 0.5, 0.0, 0.03953160345554352, 1.0, 0.5, 0.0]

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'PClw'
pClwPWF = GetOpacityTransferFunction('PClw')

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'PGraupel']

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
pClwLUT.RescaleTransferFunction(1.3887943746404563e-11, 0.03953160345554352)

# Rescale transfer function
pClwPWF.RescaleTransferFunction(1.3887943746404563e-11, 0.03953160345554352)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# create a new 'Contour'
contour2 = Contour(registrationName='Contour2', Input=iDA_2021_0829_all_data_c29nc_2)
contour2.ContourBy = ['POINTS', 'PClw']
contour2.Isosurfaces = [0.03952397406795624]
contour2.PointMergeMethod = 'Uniform Binning'

# show data in view
contour2Display = Show(contour2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.ColorArrayName = ['POINTS', 'PClw']
contour2Display.LookupTable = pClwLUT
contour2Display.SelectTCoordArray = 'None'
contour2Display.SelectNormalArray = 'Normals'
contour2Display.SelectTangentArray = 'None'
contour2Display.OSPRayScaleArray = 'PClw'
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'None'
contour2Display.ScaleFactor = 20.319801139831544
contour2Display.SelectScaleArray = 'PClw'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'PClw'
contour2Display.GaussianRadius = 1.0159900569915772
contour2Display.SetScaleArray = ['POINTS', 'PClw']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = ['POINTS', 'PClw']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [0.03952397406101227, 0.0, 0.5, 0.0, 0.03953160345554352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [0.03952397406101227, 0.0, 0.5, 0.0, 0.03953160345554352, 1.0, 0.5, 0.0]

# show color bar/color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour2
contour2.ContourBy = ['POINTS', 'PRain']

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# Properties modified on contour1
contour1.Isosurfaces = [0.05]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour2)

# Properties modified on contour2
contour2.Isosurfaces = [0.01]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(contour2)

# set active source
SetActiveSource(contour1)

# set scalar coloring
ColorBy(contour1Display, ('POINTS', 'PGraupel'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pClwLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'PGraupel'
pGraupelLUT = GetColorTransferFunction('PGraupel')

# get opacity transfer function/opacity map for 'PGraupel'
pGraupelPWF = GetOpacityTransferFunction('PGraupel')

# set active source
SetActiveSource(contour2)

# set scalar coloring
ColorBy(contour2Display, ('POINTS', 'PRain'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pClwLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'PRain'
pRainLUT = GetColorTransferFunction('PRain')

# get opacity transfer function/opacity map for 'PRain'
pRainPWF = GetOpacityTransferFunction('PRain')

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(contour2)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay.DataAxesGrid
iDA_2021_0829_all_data_c29ncDisplay.DataAxesGrid.GridAxesVisibility = 1

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# change representation type
iDA_2021_0829_all_data_c29nc_2Display.SetRepresentationType('Volume')

# change representation type
iDA_2021_0829_all_data_c29nc_2Display.SetRepresentationType('Slice')

# change representation type
iDA_2021_0829_all_data_c29nc_2Display.SetRepresentationType('Surface')

# change representation type
iDA_2021_0829_all_data_c29nc_2Display.SetRepresentationType('Outline')

# Properties modified on iDA_2021_0829_all_data_c29nc_2Display
iDA_2021_0829_all_data_c29nc_2Display.OSPRayUseScaleArray = 'All Exact'

# Properties modified on iDA_2021_0829_all_data_c29nc_2Display.DataAxesGrid
iDA_2021_0829_all_data_c29nc_2Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on iDA_2021_0829_all_data_c29nc_2Display.DataAxesGrid
iDA_2021_0829_all_data_c29nc_2Display.DataAxesGrid.GridAxesVisibility = 0

# Properties modified on iDA_2021_0829_all_data_c29nc_2Display.DataAxesGrid
iDA_2021_0829_all_data_c29nc_2Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on renderView1
renderView1.HiddenLineRemoval = 1

# Properties modified on renderView1
renderView1.HiddenLineRemoval = 0

# set active source
SetActiveSource(contour1)

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=contour1)
transform1.Transform = 'Transform'

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=contour2)
transform2.Transform = 'Transform'

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = ['POINTS', 'PGraupel']
transform1Display.LookupTable = pGraupelLUT
transform1Display.SelectTCoordArray = 'None'
transform1Display.SelectNormalArray = 'Normals'
transform1Display.SelectTangentArray = 'None'
transform1Display.OSPRayScaleArray = 'PGraupel'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 14.03175621032715
transform1Display.SelectScaleArray = 'PGraupel'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'PGraupel'
transform1Display.GaussianRadius = 0.7015878105163574
transform1Display.SetScaleArray = ['POINTS', 'PGraupel']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'PGraupel']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [0.05000000074505806, 0.0, 0.5, 0.0, 0.05000763013958931, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [0.05000000074505806, 0.0, 0.5, 0.0, 0.05000763013958931, 1.0, 0.5, 0.0]

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# show data in view
transform2Display = Show(transform2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform2Display.Representation = 'Surface'
transform2Display.ColorArrayName = ['POINTS', 'PRain']
transform2Display.LookupTable = pRainLUT
transform2Display.SelectTCoordArray = 'None'
transform2Display.SelectNormalArray = 'Normals'
transform2Display.SelectTangentArray = 'None'
transform2Display.OSPRayScaleArray = 'PRain'
transform2Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform2Display.SelectOrientationVectors = 'None'
transform2Display.ScaleFactor = 21.5
transform2Display.SelectScaleArray = 'PRain'
transform2Display.GlyphType = 'Arrow'
transform2Display.GlyphTableIndexArray = 'PRain'
transform2Display.GaussianRadius = 1.075
transform2Display.SetScaleArray = ['POINTS', 'PRain']
transform2Display.ScaleTransferFunction = 'PiecewiseFunction'
transform2Display.OpacityArray = ['POINTS', 'PRain']
transform2Display.OpacityTransferFunction = 'PiecewiseFunction'
transform2Display.DataAxesGrid = 'GridAxesRepresentation'
transform2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform2Display.ScaleTransferFunction.Points = [0.009999999776482582, 0.0, 0.5, 0.0, 0.010001907125115395, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform2Display.OpacityTransferFunction.Points = [0.009999999776482582, 0.0, 0.5, 0.0, 0.010001907125115395, 1.0, 0.5, 0.0]

# show color bar/color legend
transform2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(transform2)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# show data in view
transform2Display = Show(transform2, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(contour2, renderView1)

# show color bar/color legend
transform2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour2)

# show data in view
contour2Display = Show(contour2, renderView1, 'GeometryRepresentation')

# show color bar/color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(contour1)

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pTempLUT.ApplyPreset('Cold and Hot', True)

# Properties modified on pTempLUT
pTempLUT.AutomaticRescaleRangeMode = "Update on 'Apply'"

# Properties modified on pTempLUT
pTempLUT.InterpretValuesAsCategories = 1

# Properties modified on pTempLUT
pTempLUT.InterpretValuesAsCategories = 0

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# set active source
SetActiveSource(contour1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pGraupelLUT.ApplyPreset('Cold and Hot', True)

# set active source
SetActiveSource(contour2)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Cold and Hot', True)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, 90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, 90.0, 90.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, -90.0, 90.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, 90.0, 90.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform1.Transform
transform1.Transform.Translate = [20.0, 0.0, 0.0]
transform1.Transform.Rotate = [0.0, 0.0, 90.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform1.Transform
transform1.Transform.Translate = [76.75071237240323, 12.86608820046294, 45.94890902362047]
transform1.Transform.Rotate = [-12.120594337870468, -90.0, 6.062647368676099]
transform1.Transform.Scale = [1.0000000000000202, 1.0000000000000113, 1.0000000000000082]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [70.36611794283931, 13.048438689133107, 34.20706316662361]
transform1.Transform.Rotate = [-7.22755537150391, -85.99380524347565, 4.348543869974202]
transform1.Transform.Scale = [1.0000000000000164, 1.000000000000012, 1.0000000000000082]

# Properties modified on transform2.Transform
transform2.Transform.Translate = [1.9824126273020113, -8.78458453984996, 8.052518043761083]
transform2.Transform.Rotate = [-8.063986021744997, -90.28237177623305, 1.5410375936507825]
transform2.Transform.Scale = [1.0000000000000022, 0.999999999999999, 0.9999999999999993]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Translate = [-12.891592489427552, 22.944650940331332, -21.686776261202468]
transform2.Transform.Rotate = [0.0, -90.0, 0.0]
transform2.Transform.Scale = [1.0000000000000022, 1.0000000000000007, 0.9999999999999999]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Translate = [0.0, 22.944650940331332, -21.686776261202468]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Translate = [0.0, 0.0, -21.686776261202468]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Translate = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Translate = [200.0, 0.0, 0.0]
transform2.Transform.Scale = [1.0000000000000004, 1.0000000000000004, 1.0000000000000007]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [200.0, 0.0, 0.0]
transform1.Transform.Rotate = [0.0, -90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, -180.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [0.0, -180.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [0.0, 90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [90.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Translate = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, 90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform1.Transform
transform1.Transform.Translate = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# rescale color and/or opacity maps used to exactly fit the current data range
transform2Display.RescaleTransferFunctionToDataRange(False, True)

# Properties modified on renderView1
renderView1.UseColorPaletteForBackground = 0

# Properties modified on renderView1
renderView1.UseColorPaletteForBackground = 1

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [0.0, 0.0, 90.0]

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [0.0, 0.0, 180.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform1)

# set active source
SetActiveSource(transform2)

# set active source
SetActiveSource(transform1)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(transform1)

# set active source
SetActiveSource(transform2)

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [0.0, 90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# set active source
SetActiveSource(transform2)

# set active source
SetActiveSource(contour2)

# hide data in view
Hide(transform2, renderView1)

# show data in view
contour2Display = Show(contour2, renderView1, 'GeometryRepresentation')

# show color bar/color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# destroy transform2
Delete(transform2)
del transform2

# set active source
SetActiveSource(transform1)

# set active source
SetActiveSource(contour1)

# hide data in view
Hide(transform1, renderView1)

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# destroy transform1
Delete(transform1)
del transform1

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(contour1)

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=contour1)
transform1.Transform = 'Transform'

# set active source
SetActiveSource(transform1)

# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = ['POINTS', 'PGraupel']
transform1Display.LookupTable = pGraupelLUT
transform1Display.SelectTCoordArray = 'None'
transform1Display.SelectNormalArray = 'Normals'
transform1Display.SelectTangentArray = 'None'
transform1Display.OSPRayScaleArray = 'PGraupel'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 14.03175621032715
transform1Display.SelectScaleArray = 'PGraupel'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'PGraupel'
transform1Display.GaussianRadius = 0.7015878105163574
transform1Display.SetScaleArray = ['POINTS', 'PGraupel']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'PGraupel']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [0.05000000074505806, 0.0, 0.5, 0.0, 0.05000763013958931, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [0.05000000074505806, 0.0, 0.5, 0.0, 0.05000763013958931, 1.0, 0.5, 0.0]

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [137.07673922341925, 13.68450646182258, -0.4985875373793789]
transform1.Transform.Rotate = [0.0, -90.0, 0.0]
transform1.Transform.Scale = [0.9999999999999964, 1.000000000000003, 1.0000000000000049]

# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# set active source
SetActiveSource(contour2)

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=contour2)
transform2.Transform = 'Transform'

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform2)

# show data in view
transform2Display = Show(transform2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform2Display.Representation = 'Surface'
transform2Display.ColorArrayName = ['POINTS', 'PRain']
transform2Display.LookupTable = pRainLUT
transform2Display.SelectTCoordArray = 'None'
transform2Display.SelectNormalArray = 'Normals'
transform2Display.SelectTangentArray = 'None'
transform2Display.OSPRayScaleArray = 'PRain'
transform2Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform2Display.SelectOrientationVectors = 'None'
transform2Display.ScaleFactor = 21.5
transform2Display.SelectScaleArray = 'PRain'
transform2Display.GlyphType = 'Arrow'
transform2Display.GlyphTableIndexArray = 'PRain'
transform2Display.GaussianRadius = 1.075
transform2Display.SetScaleArray = ['POINTS', 'PRain']
transform2Display.ScaleTransferFunction = 'PiecewiseFunction'
transform2Display.OpacityArray = ['POINTS', 'PRain']
transform2Display.OpacityTransferFunction = 'PiecewiseFunction'
transform2Display.DataAxesGrid = 'GridAxesRepresentation'
transform2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform2Display.ScaleTransferFunction.Points = [0.009999999776482582, 0.0, 0.5, 0.0, 0.010001907125115395, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform2Display.OpacityTransferFunction.Points = [0.009999999776482582, 0.0, 0.5, 0.0, 0.010001907125115395, 1.0, 0.5, 0.0]

# show color bar/color legend
transform2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Translate = [137.07673922341925, 13.68450646182258, -0.4985875373793789]
transform2.Transform.Rotate = [0.0, -90.0, 0.0]

# show data in view
transform2Display = Show(transform2, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(contour2, renderView1)

# show color bar/color legend
transform2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2.Transform
transform2.Transform.Translate = [150.0, 13.68450646182258, -0.4985875373793789]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 13.68450646182258, -0.4985875373793789]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# show data in view
contour2Display = Show(contour2, renderView1, 'GeometryRepresentation')

# show color bar/color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(contour2)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [144.57445900032457, 11.699686706166936, -7.133105866056447]
transform1.Transform.Rotate = [-1.3698342199908535, -90.0, -0.19005671415366265]
transform1.Transform.Scale = [0.9999999999999972, 1.0000000000000022, 1.000000000000006]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 11.699686706166936, -7.133105866056447]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, -90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 13.68450646182258, -0.4985875373793789]

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(contour1, renderView1)

# hide data in view
Hide(contour2, renderView1)

# get color legend/bar for rRLUT in view renderView1
rRLUTColorBar = GetScalarBar(rRLUT, renderView1)

# change scalar bar placement
rRLUTColorBar.WindowLocation = 'Any Location'
rRLUTColorBar.Position = [0.7769077448747153, 0.03537284894837478]
rRLUTColorBar.ScalarBarLength = 0.32999999999999996

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 4.293643893690735, 3.9336582513530303]
transform1.Transform.Rotate = [-3.290720565541848, -90.90638558307224, -3.408576428423423]
transform1.Transform.Scale = [0.9999999999999969, 1.000000000000001, 1.0000000000000078]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 13.68450646182258, 3.9336582513530303]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 13.68450646182258, -0.4985875373793789]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, -90.90638558307224, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, -90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 13.68450646182258, -50.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Translate = [150.0, 13.68450646182258, -50.0]

# update the view to ensure updated data information
renderView1.Update()

# change scalar bar placement
rRLUTColorBar.Position = [0.7337900002644333, 0.23422562141491404]
rRLUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
rRLUTColorBar.Orientation = 'Vertical'
rRLUTColorBar.Position = [0.03561421253640687, 0.2590822179732314]
rRLUTColorBar.ScalarBarLength = 0.33000000000000007

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Blue Orange (divergent)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Inferno (matplotlib)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Black-Body Radiation', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Cool to Warm (Extended)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Rainbow Uniform', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Turbo', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Cold and Hot', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Blue Orange (divergent)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Inferno (matplotlib)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Blue Orange (divergent)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Cold and Hot', True)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pGraupelLUT.ApplyPreset('Cold and Hot', True)

# set active source
SetActiveSource(contour1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pRainLUT.ApplyPreset('Cold and Hot', True)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [150.0, 15.0, -50.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Translate = [150.0, 15.0, -50.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on transform2Display
transform2Display.OSPRayUseScaleArray = 'All Exact'

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on transform2.Transform
transform2.Transform.Translate = [-50.0, 15.0, -50.0]
transform2.Transform.Rotate = [0.0, 90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [-50.0, 15.0, -50.0]
transform1.Transform.Rotate = [0.0, 90.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Scale = [1.0, 1.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
transform1Display.RescaleTransferFunctionToDataRange(False, True)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# rescale color and/or opacity maps used to exactly fit the current data range
transform2Display.RescaleTransferFunctionToDataRange(False, True)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(contour2)

# rescale color and/or opacity maps used to exactly fit the current data range
contour2Display.RescaleTransferFunctionToDataRange(False, True)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'YZ Plane'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'XZ Plane'

# Properties modified on transform2.Transform
transform2.Transform.Translate = [-60.0, 15.0, -50.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'XY Plane'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.OSPRayUseScaleArray = 'All Exact'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'XZ Plane'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'XY Plane'

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.UseCustomBounds = 1
renderView1.AxesGrid.CustomBounds = [0.0, 180.0, 0.0, 1.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 100.0, 0.0, 1.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 200.0, 0.0, 1.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [-200.0, 200.0, 0.0, 1.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 200.0, 0.0, 1.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 100.0, 0.0, 1.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 100.0, 0.0, 180.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 100.0, 0.0, 200.0, 0.0, 1.0]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 100.0, 0.0, 200.0, 0.0, 0.5]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.CustomBounds = [0.0, 100.0, 0.0, 200.0, 0.0, 200.0]

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# change scalar bar placement
rRLUTColorBar.Position = [0.7686158709111995, 0.0908221797323136]
rRLUTColorBar.ScalarBarLength = 0.33000000000000007

# change scalar bar placement
rRLUTColorBar.Position = [0.7802244944601215, 0.0659655831739962]
rRLUTColorBar.ScalarBarLength = 0.3300000000000001

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'YZ Plane'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'XY Plane'

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# Properties modified on transform2.Transform
transform2.Transform.Translate = [-50.0, 15.0, -50.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'YZ Plane'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'XZ Plane'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.Slice = 14

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.Slice = 215

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.Slice = 0

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.SliceMode = 'XY Plane'

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.Slice = 100

# Properties modified on iDA_2021_0829_all_data_c29ncDisplay
iDA_2021_0829_all_data_c29ncDisplay.Slice = 0

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# Show orientation axes
renderView1.OrientationAxesVisibility = 1

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# Show center axes
renderView1.CenterAxesVisibility = 1

# update center of rotation
renderView1.CenterOfRotation = [49.5, 47.5, 107.5]

# Show orientation axes
renderView1.OrientationAxesVisibility = 1

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# Show orientation axes
renderView1.OrientationAxesVisibility = 1

# Hide center axes
renderView1.CenterAxesVisibility = 0

# create a new 'NetCDF Reader'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc = NetCDFReader(registrationName='IDA_2021_08-29_all_data__s202108290720320_e202108290721036_c20210830094822.nc', FileName=['/Users/sophiahu/HurricaneVis/IDA_2021_08-29_all_data__s202108290720320_e202108290721036_c20210830094822.nc'])
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc.Dimensions = '(Scanline, Field_of_view, Channel)'

# show data in view
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay = Show(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.Representation = 'Outline'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.ColorArrayName = [None, '']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SelectTCoordArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SelectNormalArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SelectTangentArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.OSPRayScaleArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SelectOrientationVectors = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.ScaleFactor = 9.5
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SelectScaleArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.GlyphType = 'Arrow'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.GlyphTableIndexArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.GaussianRadius = 0.47500000000000003
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SetScaleArray = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.OpacityArray = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.PolarAxes = 'PolarAxesRepresentation'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.ScalarOpacityUnitDistance = 3.4972727337959113
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.OpacityArrayName = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SliceFunction = 'Plane'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.Slice = 5

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.ScaleTransferFunction.Points = [155.0, 0.0, 0.5, 0.0, 285.99, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.OpacityTransferFunction.Points = [155.0, 0.0, 0.5, 0.0, 285.99, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SliceFunction.Origin = [10.5, 47.5, 5.5]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SliceFunction)

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.Slice = 0

# set scalar coloring
ColorBy(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay, ('POINTS', 'RR'))

# rescale color and/or opacity maps used to exactly fit the current data range
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SetScalarBarVisibility(renderView1, True)

# change representation type
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SetRepresentationType('Slice')

# change representation type
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SetRepresentationType('Surface')

# change representation type
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SetRepresentationType('Slice')

# create a new 'NetCDF Reader'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1 = NetCDFReader(registrationName='IDA_2021_08-29_all_data__s202108290720320_e202108290721036_c20210830094822.nc', FileName=['/Users/sophiahu/HurricaneVis/IDA_2021_08-29_all_data__s202108290720320_e202108290721036_c20210830094822.nc'])
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1.Dimensions = '(Scanline, Field_of_view, Channel)'

# show data in view
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display = Show(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.Representation = 'Outline'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.ColorArrayName = [None, '']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SelectTCoordArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SelectNormalArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SelectTangentArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.OSPRayScaleArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SelectOrientationVectors = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.ScaleFactor = 9.5
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SelectScaleArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.GlyphType = 'Arrow'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.GlyphTableIndexArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.GaussianRadius = 0.47500000000000003
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SetScaleArray = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.ScaleTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.OpacityArray = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.OpacityTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.DataAxesGrid = 'GridAxesRepresentation'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.PolarAxes = 'PolarAxesRepresentation'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.ScalarOpacityUnitDistance = 3.4972727337959113
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.OpacityArrayName = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction = 'Plane'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.Slice = 5

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.ScaleTransferFunction.Points = [155.0, 0.0, 0.5, 0.0, 285.99, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.OpacityTransferFunction.Points = [155.0, 0.0, 0.5, 0.0, 285.99, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction.Origin = [10.5, 47.5, 5.5]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# show data in view
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display = Show(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1, renderView1, 'UniformGridRepresentation')

# set scalar coloring
ColorBy(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display, ('POINTS', 'PTemp'))

# rescale color and/or opacity maps used to exactly fit the current data range
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Contour'
contour1_1 = Contour(registrationName='Contour1', Input=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)
contour1_1.ContourBy = ['POINTS', 'PClw']
contour1_1.Isosurfaces = [0.02920055948892239]
contour1_1.PointMergeMethod = 'Uniform Binning'

# show data in view
contour1_1Display = Show(contour1_1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1_1Display.Representation = 'Surface'
contour1_1Display.ColorArrayName = ['POINTS', 'PClw']
contour1_1Display.LookupTable = pClwLUT
contour1_1Display.SelectTCoordArray = 'None'
contour1_1Display.SelectNormalArray = 'Normals'
contour1_1Display.SelectTangentArray = 'None'
contour1_1Display.OSPRayScaleArray = 'PClw'
contour1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1_1Display.SelectOrientationVectors = 'None'
contour1_1Display.ScaleFactor = 1.0086576461791992
contour1_1Display.SelectScaleArray = 'PClw'
contour1_1Display.GlyphType = 'Arrow'
contour1_1Display.GlyphTableIndexArray = 'PClw'
contour1_1Display.GaussianRadius = 0.05043288230895996
contour1_1Display.SetScaleArray = ['POINTS', 'PClw']
contour1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1_1Display.OpacityArray = ['POINTS', 'PClw']
contour1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1_1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1_1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1_1Display.ScaleTransferFunction.Points = [0.029200559481978416, 0.0, 0.5, 0.0, 0.02920437417924404, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1_1Display.OpacityTransferFunction.Points = [0.029200559481978416, 0.0, 0.5, 0.0, 0.02920437417924404, 1.0, 0.5, 0.0]

# show color bar/color legend
contour1_1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
pClwLUT.RescaleTransferFunction(1.3887943746404563e-11, 0.02920437417924404)

# Rescale transfer function
pClwPWF.RescaleTransferFunction(1.3887943746404563e-11, 0.02920437417924404)

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# set active source
SetActiveSource(contour1_1)

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# set active source
SetActiveSource(contour1_1)

# set scalar coloring
ColorBy(contour1_1Display, ('POINTS', 'PGraupel'))

# rescale color and/or opacity maps used to exactly fit the current data range
contour1_1Display.RescaleTransferFunctionToDataRange(False, True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pClwLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour1_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1_1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'NetCDF Reader'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2 = NetCDFReader(registrationName='IDA_2021_08-29_all_data__s202108290720320_e202108290721036_c20210830094822.nc', FileName=['/Users/sophiahu/HurricaneVis/IDA_2021_08-29_all_data__s202108290720320_e202108290721036_c20210830094822.nc'])
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2.Dimensions = '(Scanline, Field_of_view, Channel)'

# show data in view
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display = Show(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.Representation = 'Outline'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.ColorArrayName = [None, '']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SelectTCoordArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SelectNormalArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SelectTangentArray = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.OSPRayScaleArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SelectOrientationVectors = 'None'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.ScaleFactor = 9.5
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SelectScaleArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.GlyphType = 'Arrow'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.GlyphTableIndexArray = 'BT'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.GaussianRadius = 0.47500000000000003
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SetScaleArray = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.ScaleTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.OpacityArray = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.OpacityTransferFunction = 'PiecewiseFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.DataAxesGrid = 'GridAxesRepresentation'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.PolarAxes = 'PolarAxesRepresentation'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.ScalarOpacityUnitDistance = 3.4972727337959113
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.OpacityArrayName = ['POINTS', 'BT']
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction = 'Plane'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.Slice = 5

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.ScaleTransferFunction.Points = [155.0, 0.0, 0.5, 0.0, 285.99, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.OpacityTransferFunction.Points = [155.0, 0.0, 0.5, 0.0, 285.99, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction.Origin = [10.5, 47.5, 5.5]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# show data in view
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display = Show(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2, renderView1, 'UniformGridRepresentation')

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# set scalar coloring
ColorBy(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display, ('POINTS', 'PTemp'))

# rescale color and/or opacity maps used to exactly fit the current data range
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Contour'
contour2_1 = Contour(registrationName='Contour2', Input=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)
contour2_1.ContourBy = ['POINTS', 'PClw']
contour2_1.Isosurfaces = [0.02920055948892239]
contour2_1.PointMergeMethod = 'Uniform Binning'

# show data in view
contour2_1Display = Show(contour2_1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour2_1Display.Representation = 'Surface'
contour2_1Display.ColorArrayName = ['POINTS', 'PClw']
contour2_1Display.LookupTable = pClwLUT
contour2_1Display.SelectTCoordArray = 'None'
contour2_1Display.SelectNormalArray = 'Normals'
contour2_1Display.SelectTangentArray = 'None'
contour2_1Display.OSPRayScaleArray = 'PClw'
contour2_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2_1Display.SelectOrientationVectors = 'None'
contour2_1Display.ScaleFactor = 1.0086576461791992
contour2_1Display.SelectScaleArray = 'PClw'
contour2_1Display.GlyphType = 'Arrow'
contour2_1Display.GlyphTableIndexArray = 'PClw'
contour2_1Display.GaussianRadius = 0.05043288230895996
contour2_1Display.SetScaleArray = ['POINTS', 'PClw']
contour2_1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2_1Display.OpacityArray = ['POINTS', 'PClw']
contour2_1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2_1Display.DataAxesGrid = 'GridAxesRepresentation'
contour2_1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2_1Display.ScaleTransferFunction.Points = [0.029200559481978416, 0.0, 0.5, 0.0, 0.02920437417924404, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2_1Display.OpacityTransferFunction.Points = [0.029200559481978416, 0.0, 0.5, 0.0, 0.02920437417924404, 1.0, 0.5, 0.0]

# show color bar/color legend
contour2_1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(contour1_1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pGraupelLUT.ApplyPreset('Cold and Hot', True)

# set active source
SetActiveSource(contour2_1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pClwLUT.ApplyPreset('Cold and Hot', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pClwLUT.ApplyPreset('Black-Body Radiation', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pClwLUT.ApplyPreset('Cool to Warm', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pClwLUT.ApplyPreset('Inferno (matplotlib)', True)

# set active source
SetActiveSource(contour1_1)

# set active source
SetActiveSource(contour2_1)

# set scalar coloring
ColorBy(contour2_1Display, ('POINTS', 'PRain'))

# rescale color and/or opacity maps used to exactly fit the current data range
contour2_1Display.RescaleTransferFunctionToDataRange(False, True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pClwLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour2_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour2_1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(contour1_1)

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pTempLUT.ApplyPreset('Cold and Hot', True)

# change representation type
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SetRepresentationType('Volume')

# change representation type
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SetRepresentationType('Points')

# change representation type
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SetRepresentationType('Outline')

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# set active source
SetActiveSource(contour1_1)

# set active source
SetActiveSource(contour2_1)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=contour2_1)
threshold1.Scalars = ['POINTS', 'PRain']
threshold1.LowerThreshold = 0.009999999776482582
threshold1.UpperThreshold = 0.009999999776482582

# set active source
SetActiveSource(contour2_1)

# destroy threshold1
Delete(threshold1)
del threshold1

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)
programmableFilter1.Script = ''
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# destroy programmableFilter1
Delete(programmableFilter1)
del programmableFilter1

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# destroy iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc
Delete(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc)
del iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# set active source
SetActiveSource(contour1_1)

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display)

# hide data in view
Hide(contour1_1, renderView1)

# show data in view
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display = Show(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1, renderView1, 'UniformGridRepresentation')

# show color bar/color legend
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1Display.SetScalarBarVisibility(renderView1, True)

# destroy contour1_1
Delete(contour1_1)
del contour1_1

# destroy iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1
Delete(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1)
del iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_1

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# set active source
SetActiveSource(contour2_1)

# set active source
SetActiveSource(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display)

# hide data in view
Hide(contour2_1, renderView1)

# show data in view
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display = Show(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2, renderView1, 'UniformGridRepresentation')

# show color bar/color legend
iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2Display.SetScalarBarVisibility(renderView1, True)

# destroy contour2_1
Delete(contour2_1)
del contour2_1

# destroy iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2
Delete(iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2)
del iDA_2021_0829_all_data__s202108290720320_e202108290721036_c20210830094822nc_2

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(contour2)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(transform2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(contour2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_2Display)

# set active source
SetActiveSource(transform1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(contour1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# change scalar bar placement
rRLUTColorBar.Position = [0.7912121335599694, 0.07769967392080482]

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc_1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29nc_1Display)

# set active source
SetActiveSource(iDA_2021_0829_all_data_c29nc)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=iDA_2021_0829_all_data_c29ncDisplay)

# rescale color and/or opacity maps used to exactly fit the current data range
iDA_2021_0829_all_data_c29ncDisplay.RescaleTransferFunctionToDataRange(False, True)

# get color legend/bar for pTempLUT in view renderView1
pTempLUTColorBar = GetScalarBar(pTempLUT, renderView1)

# change scalar bar placement
pTempLUTColorBar.WindowLocation = 'Any Location'
pTempLUTColorBar.Position = [0.56841046277666, 0.7982485619250278]

# set scalar coloring
ColorBy(iDA_2021_0829_all_data_c29ncDisplay, ('POINTS', 'GWP'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(rRLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data_c29ncDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data_c29ncDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'GWP'
gWPLUT = GetColorTransferFunction('GWP')

# get opacity transfer function/opacity map for 'GWP'
gWPPWF = GetOpacityTransferFunction('GWP')

# set scalar coloring
ColorBy(iDA_2021_0829_all_data_c29ncDisplay, ('POINTS', 'RR'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(gWPLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
iDA_2021_0829_all_data_c29ncDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
iDA_2021_0829_all_data_c29ncDisplay.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for pGraupelLUT in view renderView1
pGraupelLUTColorBar = GetScalarBar(pGraupelLUT, renderView1)

# change scalar bar placement
pGraupelLUTColorBar.WindowLocation = 'Any Location'
pGraupelLUTColorBar.Position = [0.03219315895372232, 0.10268714011516317]
pGraupelLUTColorBar.ScalarBarLength = 0.33

# get color legend/bar for pRainLUT in view renderView1
pRainLUTColorBar = GetScalarBar(pRainLUT, renderView1)

# change scalar bar placement
pRainLUTColorBar.WindowLocation = 'Any Location'
pRainLUTColorBar.Position = [0.07444668008048291, 0.6122840690978887]
pRainLUTColorBar.ScalarBarLength = 0.32999999999999996

# change scalar bar placement
pRainLUTColorBar.Position = [0.03018108651911469, 0.6333973128598849]

# change scalar bar placement
pTempLUTColorBar.Position = [0.6207243460764588, 0.8443138210421104]

# change scalar bar placement
pGraupelLUTColorBar.Position = [0.022505322570514574, 0.26391554702495207]
pGraupelLUTColorBar.ScalarBarLength = 0.3299999999999999

# change scalar bar placement
pGraupelLUTColorBar.Position = [0.030040306424120602, 0.26007677543186186]
pGraupelLUTColorBar.ScalarBarLength = 0.3299999999999998

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1858, 1042)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-400.17146002147575, 154.05707249851466, -976.0368493406004]
renderView1.CameraFocalPoint = [57.49999999999997, 107.5, 33.04299999999997]
renderView1.CameraViewUp = [0.22444354410716272, 0.9728237386598036, -0.0569128193694358]
renderView1.CameraParallelScale = 237.2143571645696

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).