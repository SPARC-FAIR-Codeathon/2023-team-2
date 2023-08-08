# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:12:26 2023

@author: moscr
"""

#%% First we need to download a neuron model. This can be done using AllenSDK.

# The following commands will create a new directory (neuronal_model folder), and download the neuron model with ID=626170421
# pip install bmtk 
# pip install allensdk
from allensdk.api.queries.biophysical_api import BiophysicalApi

bp = BiophysicalApi()
bp.cache_stimulus = False        # Skip the large stimulus file download
neuronal_model_id = 626170421
bp.cache_data(neuronal_model_id, working_directory='neuronal_model')
#%%  Next, we run a simple simulation to obtain some data.

# First thing is to create a network. The following commands will set up a single cell network.
from bmtk.builder.networks import NetworkBuilder


net = NetworkBuilder('single_neuron')
net.add_nodes(cell_name='Cell_571718621',
              potental='exc',
              model_type='biophysical',
              model_template='ctdb:Biophys1.hoc',
              model_processing='aibs_perisomatic',
              dynamics_params='571718621_fit.json',
              morphology='H17.06.006.11.08.08_601946464_m.swc')

net.build()
net.save_nodes(output_dir='Model')        
        
#%% Second, we can set up a simulation. The following commands set up a direct current injection simulation of 120pA amplitude and 10s duration at the soma of the neuron.

from bmtk.utils.sim_setup import build_env_bionet

build_env_bionet(
    base_dir='Simulation',     # Where to save the scripts and config files
    config_file='config.json', # Where main config will be saved.
    network_dir='Model',       # Location of directory containing network files
    tstop=15000.0, dt=0.1,     # Run a simulation for 15s at 0.1 ms intervals
    report_vars=['v', 'cai'],  # Tells simulator we want to record membrane potential and calcium traces
    current_clamp={            # Creates a step current from 1s to 11s
        'amp': 0.120,
        'delay': 1000.0,
        'duration': 10000.0
    },
    include_examples=False,    # Will not copies components files for tutorial examples
    compile_mechanisms=False   # Will NOT try to compile NEURON mechanisms
)
        
        
#%% Before we run the simulation, we need to provide the component files and compile the NEURON mechanisms. The following commands should handle this (working with Windows)

import shutil
import os
from subprocess import call

#Copy component files
shutil.copyfile('./neuronal_model/571718621_fit.json', './Simulation/components/biophysical_neuron_models/571718621_fit.json')
shutil.copyfile('./neuronal_model/H17.06.006.11.08.08_601946464_m.swc', './Simulation/components/morphologies/H17.06.006.11.08.08_601946464_m.swc')
shutil.copytree('./neuronal_model/modfiles','./Simulation/components/mechanisms/modfiles')

#Compile mechanisms
status=call("nrnivmodl modfiles",cwd=os.getcwd()+"/Simulation/components/mechanisms",shell=True)
if status:
    print ("NEURON ERROR")
else:
    print ("Compilation done!") 
        
        
#%% Now we can run the simulation.

from bmtk.simulator import bionet

conf = bionet.Config.from_json('Simulation/config.json')
conf.build_env()
conf
net = bionet.BioNetwork.from_config(conf)
sim = bionet.BioSimulator.from_config(conf, network=net)
sim.run()


#%%   The simulation output can be plotted using the following commands.


from bmtk.analyzer.compartment import plot_traces

_ = plot_traces(config_file='Simulation/config.json', node_ids=[0], report_name='v_report')

#%%  Now we can create the animation visualizing the soma potential in color.

# The following commands should create the animation.gif file.

       
        
        
        
from bmtk.utils.sonata.config import SonataConfig
import bmtk.analyzer.compartment as ancomp
import bmtk.utils.reports.compartment.plotting as bplt
from bmtk.utils.reports.compartment.compartment_report import CompartmentReport
import neurom as nm #https://neurom.readthedocs.io/en/stable/examples.html
import neurom.view.matplotlib_impl as mplt
from neurom.view import matplotlib_utils
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as cl
import matplotlib.cm as cm
import numpy as np

# Create figure for plotting
fig, ax = plt.subplots(nrows=1,ncols=2, figsize=(13, 5),gridspec_kw={'width_ratios': [1, 1.5]})

# Draw neuron morph (based on neurom)
m = nm.load_morphology('./neuronal_model/H17.06.006.11.08.08_601946464_m.swc')
m.name='Neuron'
mplt.plot_morph(m,ax=ax[0],neurite_type=nm.NeuriteType.all,plane='xy',soma_outline=True,diameter_scale=1.0,linewidth=1.2,color='blue',alpha=0.8,realistic_diameters=True)
matplotlib_utils.plot_style(fig=fig, ax=ax[0])
ax[0].set_ylim([300,500]) #some zoom in
ax[0].set_xlim([300,500])
fig.tight_layout(pad=3)

#select colormap for painting neuron, and map values from minimum to maxium potential (-80,20)mV
cmap = cm.get_cmap('cool')
norm = cl.Normalize(-80, 20)
color_producer = cm.ScalarMappable(norm=norm, cmap=cmap)

#get the raw simulation data
Config_file='Simulation/config.json'
Injected_current='120 mA'
Population='single_neuron'
Report='v_report'
print ('Working with '+Config_file+'(Injected current '+Injected_current+')'+', '+Population+', '+Report)
sonata_config = SonataConfig.from_json(Config_file)
report_name, cr = ancomp._get_report(report_path=None, config=sonata_config, report_name=Report)
cr=CompartmentReport.load(cr)
pop = bplt.__get_population(report=cr, population=Population)
trace_times = cr.time_trace(population=pop)
times = (trace_times[0], trace_times[-1])
trace_data = cr.data(node_id=0, sections='origin', population=pop, time_window=times)

#get neuron shapes for fast painting without redrawing
items=ax[0].get_children()
itp=[] #patches
itc=[] #circles
for i in items:
    if 'PatchCollection' in str(type(i)):
        itp.append(i)
    if 'Circle' in str(type(i)):
        itc.append(i)

#prefil some data and goto spikes istead of starting from the beginning
xs=[]
ys=[]
for i in range (19890,20000):
    xs.append(trace_times[i])
    ys.append(trace_data[i])
trace_times=trace_times[20000:]
trace_data=trace_data[20000:]

#animation initialization function to avoid double run and double data value. Otherwize animate func runs twice for i=0
#https://stackoverflow.com/questions/42989414/matplotlib-funcanimation-update-function-is-called-twice-for-first-argument
def init():
    pass

#animation function
def animate(i, xs:list, ys:list):
    xs.append(trace_times[i]) # fill new data at each iteration
    ys.append(trace_data[i])
    xs = xs[-100:] # limit x and y lists to 100 items
    ys = ys[-100:]
    ax[1].clear() # clear and redraw
    ax[1].plot(xs, ys, color=color_producer.to_rgba(int(ys[50][0])))
    ax[1].set_ylim([-80,20]) # format plot
    ax[1].set_title('Neuron response', fontsize=14)
    ax[1].set_xlabel('Time (ms)', fontsize=14)
    ax[1].set_ylabel('Soma potential (mV)', fontsize=14)
    ax[1].axvline(xs[50], linestyle='--', color='k')# draw vertical line
    for j in itp: # change neuron color according to colormap and potential value at vertical line point
        j.set_facecolor(color_producer.to_rgba(int(ys[50][0]))) #patches don't have edges, so set_facecolor
    for j in itc:
        j.set_color(color_producer.to_rgba(int(ys[50][0])))  #circles do have edges, so set_color

# Set up plot to call animate() function every 10 milliseconds
ani = animation.FuncAnimation(fig, animate, frames=150, fargs=(xs,ys),init_func=init, interval=10,repeat=False) #change frames value to change duration
ani.save('animation.gif', fps=60)
        