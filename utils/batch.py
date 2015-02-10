from numpy import array, sqrt
from utils.collect import Data, save_data
import itertools
import os


def run_base_batch(data_path, model, N, input_dim, eval_points, encs, f, stim_func,
              conn_synapse, probe_synapse, t=0.5):
    #Make all parameters lists except t and model

    print 'Initializing parameters.'
    input_dim = [x**2 for x in input_dim] 
    paramses = itertools.product(N, input_dim, eval_points, stim_func,
                                 conn_synapse, probe_synapse)
    for param in paramses:
        param = list(param)
        param.insert(2, encs(param[0], sqrt(param[1]), f))
        sim, probe = model(*param)
        print 'Running simulation.'
        sim.run(t)

        print 'Saving data.'
        save_data(data_path,
                  Data(label=os.path.basename(__file__).strip('.py').strip('.pyc'),
                       params=param,
                       data=array([opt for opt in sim.data[probe]])))
        print 'Simulation finished.'

