'''
Created on 22 jul. 2012

@author: localadmin
'''
import numpy as np
import matplotlib.pyplot as plt

from analysis.plotting import *
from analysis.plotting_util import make_continuous_grouping_specifiers,\
                          filter_scalar_outcomes, group_results, BOXPLOT, KDE,\
                          VIOLIN, HIST, LINES, ENV_LIN, ENVELOPE
from expWorkbench import load_results, ema_logging
from analysis.b_and_w_plotting import set_fig_to_bw

from analysis.pairs_plotting import pairs_scatter,\
                                     pairs_lines,\
                                     pairs_density
                                     
from test import util
                                                      
np = np
 
def test_make_continuous_grouping_specifiers():
    array = np.random.randint(1,100, size=(1000,))
    categories = make_continuous_grouping_specifiers(array, nr_of_groups=10)
    
    for entry in categories:
        print repr(entry)
    print np.min(array), np.max(array)

def test_filter_scalar_outcomes():
    outcomes = {}
    for entry in ['a', 'b', 'c']:
        outcomes[entry] = np.random.rand(10,100)
    for entry in ['d','e','f']:
        outcomes[entry] = np.random.rand(10)
    outcomes = filter_scalar_outcomes(outcomes)
    print outcomes.keys()

def test_group_results():
    results = load_results(r'./../data/eng_trans_100.cPickle', zipped=False)
    experiments, outcomes = results
    
    # test indices
    grouping_specifiers = {'set1':np.arange(0,11),
                           'set2':np.arange(11,25),
                           'set3':np.arange(25,experiments.shape[0])}
    groups = group_results(experiments, outcomes, 
                           group_by='index', 
                           grouping_specifiers=grouping_specifiers)
    total_data = 0
    for value in groups.values():
        total_data += value[0].shape[0]
    print experiments.shape[0], total_data
    
    # test continuous parameter type
    array = experiments['average planning and construction period T1']
    grouping_specifiers = make_continuous_grouping_specifiers(array, nr_of_groups=5)
    groups = group_results(experiments, outcomes, 
                           group_by='average planning and construction period T1', 
                           grouping_specifiers=grouping_specifiers) 
    total_data = 0
    for value in groups.values():
        total_data += value[0].shape[0]
    print experiments.shape[0], total_data   
    
    # test integer type
    array = experiments['seed PR T1']
    grouping_specifiers = make_continuous_grouping_specifiers(array, nr_of_groups=10)
    groups = group_results(experiments, outcomes, 
                           group_by='seed PR T1', 
                           grouping_specifiers=grouping_specifiers) 
    total_data = 0
    for value in groups.values():
        total_data += value[0].shape[0]
    print experiments.shape[0], total_data   

    
    # test categorical type
    grouping_specifiers = set(experiments["policy"])
    groups = group_results(experiments, outcomes, 
                       group_by='policy', 
                       grouping_specifiers=grouping_specifiers)
    total_data = 0
    for value in groups.values():
        total_data += value[0].shape[0]
    print experiments.shape[0], total_data   

def test_lines():
    results = util.load_eng_trans_data()

#     lines(results, 
#           outcomes_to_show="total fraction new technologies",
#           experiments_to_show=np.arange(0,600, 20),
#           group_by='policy',
#           grouping_specifiers = 'basic policy'
#           )
#     lines(results, 
#           experiments_to_show=np.arange(0,600, 2),
#           group_by='policy',
#           density=HIST
#           )
#     lines(results, 
#           experiments_to_show=np.arange(0,600, 2),
#           group_by='policy',
#           density=KDE
#           )
#     lines(results, 
#           experiments_to_show=np.arange(0,600, 2),
#           group_by='policy',
#           density=BOXPLOT
#           )
#     lines(results, 
#           experiments_to_show=np.arange(0,600, 2),
#           group_by='policy',
#           density=VIOLIN
#           )
#     lines(results, 
#           group_by='index',
#           grouping_specifiers = {"blaat": np.arange(1, 100, 2)},
#           density=KDE,
#           )
#      
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=KDE,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy']
          )
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=HIST,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy']
          )
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=BOXPLOT,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy']
          )
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=VIOLIN,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy']
          )
    
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=KDE,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy'],
          log=True
          )
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=HIST,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy'],
          log=True
          )
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=BOXPLOT,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy'],
          log=True
          )
    lines(results, 
          experiments_to_show=np.arange(0,600, 30),
          group_by='policy',
          density=VIOLIN,
          show_envelope=True,
          grouping_specifiers=['no policy', 'adaptive policy'],
          log=True
          )    
  
#    set_fig_to_bw(lines(results, 
#             experiments_to_show=np.arange(0,600, 20),
#             group_by='policy',
#             density=KDE
#             )[0])      
#     
#    experiments, outcomes = results
#    new_outcomes = {}
#    for key, value in outcomes.items():
#        new_outcomes[key] = value[0:20, :]
#    experiments = experiments[0:20]
#    results = experiments, new_outcomes
#       
#    #no grouping, with density
#    set_fig_to_bw(lines(results, density=KDE)[0])
#    set_fig_to_bw(lines(results, density=HIST)[0])
#    set_fig_to_bw(lines(results, density=BOXPLOT)[0])
#    set_fig_to_bw(lines(results, density=VIOLIN)[0])
#       
#    # grouping and density
#    set_fig_to_bw(lines(results, 
#          group_by='policy',
#          density='kde')[0])
#       
#    # grouping, density as histograms
#    # grouping and density
#    set_fig_to_bw(lines(results, 
#          group_by='policy',
#          density='hist',
#          legend=False)[0])

    plt.show()

def test_envelopes():
    results = util.load_eng_trans_data()
    
#     #testing titles
#     envelopes(results, 
#               density=None,
#               titles=None)
#     envelopes(results, 
#           density=None,
#           titles={})
#     envelopes(results, 
#           density=None,
#           titles={'total fraction new technologies': 'a',
#                   'total fraction new technologies': 'b'})
#  
#     #testing ylabels
#     envelopes(results, 
#               density=None,
#               ylabels=None)
#     envelopes(results, 
#           density=None,
#           ylabels={})
#     envelopes(results, 
#           density=None,
#           ylabels={'total fraction new technologies': 'a'})
#      
#     #no grouping no density
#     envelopes(results, 
#               titles=None)
#     set_fig_to_bw(envelopes(results, density=None)[0])
#      
#     #no grouping, with density
#     envelopes(results, density=KDE)
#     envelopes(results, density=HIST)
#     envelopes(results, density=BOXPLOT)
#     envelopes(results, density=VIOLIN)
#     set_fig_to_bw(envelopes(results, density=VIOLIN)[0])

    
    # grouping and density kde
#    envelopes(results, 
#              group_by='policy',
#              density=VIOLIN)
#    envelopes(results, 
#              group_by='policy',
#              density=BOXPLOT)
#    envelopes(results, 
#              group_by='policy',
#              density=KDE,
#              grouping_specifiers=['no policy', 'adaptive policy'])
#    envelopes(results, 
#              group_by='policy',
#              density=BOXPLOT,
#              grouping_specifiers=['no policy', 'adaptive policy'])
#    envelopes(results, 
#              group_by='policy',
#              density=KDE)

    envelopes(results, 
              group_by='policy',
              density=VIOLIN)
#    envelopes(results, 
#              group_by='policy',
#              density=BOXPLOT)
#    envelopes(results, 
#              group_by='policy',
#              density=KDE)          
#    envelopes(results, 
#              group_by='policy',
#              density=HIST)
    
#    envelopes(results, 
#              group_by='policy',
#              density=VIOLIN,
#              log=True)
#    envelopes(results, 
#              group_by='policy',
#              density=BOXPLOT,
#              log=True)
#    envelopes(results, 
#              group_by='policy',
#              density=KDE,
#              log=True)          
#    envelopes(results, 
#              group_by='policy',
#              density=HIST,
#              log=True)
#       
#    # grouping and density hist
#    envelopes(results, 
#              group_by='policy',
#              density=HIST)
#    envelopes(results, 
#              group_by='policy',
#              density=HIST)
#      
#    set_fig_to_bw(envelopes(results, 
#              group_by='policy',    
#              density=KDE)[0])
#      
#    # grouping and density
#    envelopes(results, 
#              group_by='policy',
#              density=KDE,
#              fill=True)
#    set_fig_to_bw(envelopes(results, 
#              group_by='policy',
#              density=KDE,
#              fill=True)[0])

    plt.show()

def test_kde_over_time():
    results = util.load_eng_trans_data()
    
#    kde_over_time(results, log=False)
#    kde_over_time(results, log=True)
    kde_over_time(results, group_by='policy', grouping_specifiers=['no policy', 'adaptive policy'])
    plt.show()

def test_pairs_lines():
    results = util.load_eng_trans_data()  
    pairs_lines(results)
#    set_fig_to_bw(pairs_lines(results)[0])
    
    pairs_lines(results, group_by='policy')
#    set_fig_to_bw(pairs_lines(results, group_by='policy')[0])
    plt.show()

def test_pairs_density():
    results =  util.load_eng_trans_data() 
#    pairs_density(results)
#    pairs_density(results, colormap='binary')

    pairs_density(results, group_by='policy', grouping_specifiers=['no policy'])
    plt.show()

def test_pairs_scatter():
    results = util.load_eng_trans_data() 
    
    pairs_scatter(results)
#    set_fig_to_bw(pairs_scatter(results)[0])
    
    pairs_scatter(results, group_by='policy',
                  grouping_specifiers='basic policy', legend=False)
#    set_fig_to_bw(pairs_scatter(results, group_by='policy')[0])
    
    pairs_scatter(results, group_by='policy', 
                  grouping_specifiers=['no policy', 'adaptive policy'])
#    set_fig_to_bw(pairs_scatter(results, group_by='policy', legend=False)[0])
    plt.show()

def test_multiple_densities():
    results = util.load_eng_trans_data()
    ooi = 'total fraction new technologies'
    
#    multiple_densities(results, 
#                  outcomes_to_show=ooi, 
#                  group_by="policy", 
#                  points_in_time = [2010])
#    multiple_densities(results, 
#                  outcomes_to_show=ooi, 
#                  group_by="policy", 
#                  points_in_time = [2010, 2100])
#    multiple_densities(results, 
#                  outcomes_to_show=ooi, 
#                  group_by="policy", 
#                  points_in_time = [2010, 2050, 2100])
#    multiple_densities(results, 
#                  outcomes_to_show=ooi, 
#                  group_by="policy", 
#                  points_in_time = [2010, 2020, 2050, 2080])
#    multiple_densities(results, 
#                  outcomes_to_show=ooi, 
#                  group_by="policy", 
#                  points_in_time = [2010, 2020, 2040, 2060, 2100])
    
    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=KDE,
                  experiments_to_show=[1,2,10])
    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=HIST,    
                  experiments_to_show=[1,2,10])
    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=BOXPLOT,
                  experiments_to_show=[1,2,10])
    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=VIOLIN,
                  experiments_to_show=[1,2,10])

    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=KDE,
                  experiments_to_show=[1,2,10],
                  log=True)
    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=HIST,    
                  experiments_to_show=[1,2,10],
                  log=True)
    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=BOXPLOT,
                  experiments_to_show=[1,2,10],
                  log=True)
    multiple_densities(results, 
                  outcomes_to_show=ooi, 
                  group_by="policy", 
                  points_in_time = [2010,2020, 2040, 2060, 2080, 2100],
                  plot_type=ENV_LIN,
                  density=VIOLIN,
                  experiments_to_show=[1,2,10],
                  log=True)

    
    plt.show()



if __name__ == '__main__':
    ema_logging.log_to_stderr(ema_logging.INFO)
#     test_lines()
#     test_envelopes()
#     test_kde_over_time()
#     test_multiple_densities()

#     test_pairs_scatter()
    test_pairs_lines()
#    test_pairs_density()

#    test_filter_scalar_outcomes()
#    test_group_results()
#    test_make_continuous_grouping_specifiers()

