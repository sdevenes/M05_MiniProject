import argparse
import configparser
import experiments, database
import os.path

parser = argparse.ArgumentParser(description='M05 mini-project: experiments')
parser.add_argument('datapath', type=str,
                    help='Dataset file in .csv')
parser.add_argument('output', type=str,
                    help='Destination folder for the results')
parser.add_argument('config', type=str,
                    help='Filepath for experiments configuration file in .ini')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config)


print('M05 mini-project on Human Activity Recognition with Random Forest classifier')
tabnum = 1
experiment_results = experiments.experiment_impact_nb_trees(
    tabnum,
    filepath=args.datapath,
    nb_trees=[int(n) for n in config['nb_trees_experiment']['nb_trees'].split(',')],
    max_depth=int(config['nb_trees_experiment']['tree_depth']),
)

tabnum += len(config['nb_trees_experiment']['nb_trees'].split(',')) * len(database.PROTOCOLS)
experiment_results += experiments.experiment_impact_tree_depth(
    tabnum,
    filepath=args.datapath,
    nb_trees=int(config['tree_depth_experiment']['nb_trees']),
    max_depths=[int(d) for d in config['tree_depth_experiment']['tree_depth'].split(',')],
)

with open(os.path.join(args.output, 'experiment_results.txt'), 'w+') as fout:
    fout.write(experiment_results)
print('Experiments done\n')
