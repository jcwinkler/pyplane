{
    "sectionlist": ["Logging", "Plotting", "Phaseplane", "x-t-plot", "y-t-plot", "System", "Vectorfield", "Streamlines",
                    "Nullclines", "Trajectories", "Functions", "Export", "Test"],

    "Logging": "Logging Behaviour",
    "log_showDbg": ["Enable debug mode", False],
    "log_showError": ["Show error messages", True],
    "log_showWarning": ["Show warnings", True],
    "log_showTime": ["Show time in log messages", True],
    "showTerminal": ["Show PyPlane terminal", True],

    "Plotting": "Change General Plotting Settings",
    "plot_background": ["Background color of plot surrounding area", "#ffffff"],
    "plot_backgroundTransparent": ["Surrounding area transparent", False],
    "plot_CanvasBackground": ["Background color of the plot", "#ffffff"],
    "plot_fontSize": ["Font size of tick markers and title", 10],
    "plot_topOfPlot": ["Space on top of the plot", 0.89],
    "plot_leftOfPlot": ["Space on the left of the plot", 0.05],
    "plot_rightOfPlot": ["Space on the right of the plot", 0.975],
    "plot_bottomOfPlot": ["Space on the bottom of the plot", 0.09],

    "Phaseplane": "Specify Phaseplane Properties",
    "pp_xmin": ["Minimum x value of the plot", -10.],
    "pp_xmax": ["Maximum x value of the plot", 10.],
    "pp_ymin": ["Minimum y value of the plot", -10.],
    "pp_ymax": ["Maximum y value of the plot", 10.],
    "pp_showXTicks": ["Show ticks on x axis", True],
    "pp_showYTicks": ["Show tick on y axis", True],
    "pp_showMinorTicks": ["Show minor ticks", True],
    "pp_showSpines": ["Show surrounding rectangle (spines)", True],
    "pp_showGrid": ["Show grid", True],
    "pp_showTitle": ["Show system in title (latex)", True],
    "pp_showXLabel": ["Show x label", False],
    "pp_showYLabel": ["Show y label", False],
    "pp_labelFontSize": ["Label font size", 12],

    "x-t-plot": "Specify x(t)-Plot Properties",
    "x_tmin": ["Minimum t value of the plot", 0.],
    "x_tmax": ["Maximum t value of the plot", 10.],
    "x_xmin": ["Minimum x value of the plot", -10.],
    "x_xmax": ["Maximum x value of the plot", 10.],
    "x_showXTicks": ["Show ticks on x axis", True],
    "x_showYTicks": ["Show tick on y axis", True],
    "x_showMinorTicks": ["Show minor ticks", True],
    "x_showSpines": ["Show surrounding rectangle (spines)", True],
    "x_showGrid": ["Show grid", True],
    "x_showTitle": ["Show system in title (latex)", False],
    "x_showXLabel": ["Show x label", True],
    "x_showYLabel": ["Show y label", True],
    "x_labelFontSize": ["Label font size", 12],

    "y-t-plot": "Specify y(t)-Plot Properties",
    "y_tmin": ["Minimum t value of the plot", 0.],
    "y_tmax": ["Maximum t value of the plot", 10.],
    "y_ymin": ["Minimum y value of the plot", -10.],
    "y_ymax": ["Maximum y value of the plot", 10.],
    "y_showXTicks": ["Show ticks on x axis", True],
    "y_showYTicks": ["Show tick on y axis", True],
    "y_showMinorTicks": ["Show minor ticks", True],
    "y_showSpines": ["Show surrounding rectangle (spines)", True],
    "y_showGrid": ["Show grid", True],
    "y_showTitle": ["Show system in title (latex)", False],
    "y_showXLabel": ["Show x label", True],
    "y_showYLabel": ["Show y label", True],
    "y_labelFontSize": ["Label font size", 12],

    "System": "Settings for Numerical Integration",
    "max_norm": ["Set norm([x,y]) threshold (see documentation)", 1e5],

    "Vectorfield": "Vectorfield Properties",
    "vf_onByDefault": ["Turn on by default", True],
    "vf_color": ["Arrow Color", "#b3b3b3"],
    "vf_gridPointsInX": ["Number of arrows in x direction", 40],
    "vf_gridPointsInY": ["Number of arrows in y direction", 20],
    "vf_arrowHeadWidth": ["Headwidth  of arrows", 2.5],
    "vf_arrowHeadLength": ["Headlength of arrows", 3.],
    "vf_arrowWidth": ["Arrow width", 0.001],
    "vf_arrowPivot": ["Pivot (point of rotation)", "middle"],

    "Streamlines": "Streamline Properties",
    "stream_onByDefault": ["Turn on by default", False],
    "stream_color": ["Color", "#b3b3b3"],
    "stream_density": ["Density of streamlines", 2.],
    "stream_linewidth": ["Linewidth", 1.],
    "stream_gridPointsInX": ["Number of grid points in x direction", 100],
    "stream_gridPointsInY": ["Number of grid points in y direction", 100],

    "Nullclines": "Nullcline Properties",
    "nc_onByDefault": ["Turn on by default", False],
    "nc_color_xdot": ["Color x-nullcline", "#ff00ff"],
    "nc_color_ydot": ["Color y-nullcline", "#ff6600"],
    "nc_linewidth": ["Linewidth", 1.],
    "nc_gridPointsInX": ["Number of grid points in x direction", 500],
    "nc_gridPointsInY": ["Number of grid points in y direction", 500],

    "Trajectories": "Trajectory Settings",
    "traj_ppForwardColor": ["Color of forward trajectories", "#0000ff"],
    "traj_ppBackwardColor": ["Color of backward trajectories", "#0000ff"],
    "traj_x_tColor": ["Color of x(t) curves", "#0000ff"],
    "traj_y_tColor": ["Color of y(t) curves", "#0000ff"],
    "traj_plotInitPoint": ["Mark initial condition", True],
    "traj_initPointColor": ["Color of initial condition", "#008000"],
    "traj_checkForwardByDefault": ["Check forward integration by default", True],
    "traj_checkBackwardByDefault": ["Check backward integration by default", True],
    "traj_integrationtime": ["Integration time (sec)", 10.],
    "traj_integrationstep": ["Integration step size (sec)", 0.0005],

    "Functions": "Function Plotting",
    "fct_gridPointsInX": ["Number of grid points in x direction", 500],
    "fct_gridPointsInY": ["Number of grid points in y direction", 500],
    "fct_linewidth": ["Linewidth", 1.],
    "fct_color": ["Color", "#ff0000"],

    "Export": "Export Settings",
    "pdf_exportInSeparateFiles": ["Export graphs in separate pdfs", False],

    "Test": "This is just for testing",
    "test_var": ["Read test variable vom config"],

}