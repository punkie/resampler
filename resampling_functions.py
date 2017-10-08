import datetime
from general_functions import write_dataset_to_csv


def do_sampling(state):
    sampling_algorithm = state.sampling_algorithm
    output_directory = state.output_dir
    dataset = state.dataset
    # X, y = make_classification(n_classes=2, class_sep=2, weights=[0.3, 0.7],
    #                            n_informative=3, n_redundant=1, flip_y=0,
    #                            n_features=20, n_clusters_per_class=1,
    #                            n_samples=80, random_state=10)
    y_values = dataset['y_values']
    x_values = dataset['x_values']
    x_resampled_values, y_resampled_values = sampling_algorithm.value[1].fit_sample(x_values, y_values)
    write_dataset_to_csv(__create_resampled_file_name(output_directory, dataset['name'], sampling_algorithm.value[0]),
                         x_values_param=x_resampled_values, y_values_param=y_resampled_values)


def __create_resampled_file_name(output_dir, dataset_name, algorithm_name):
    time = str(datetime.datetime.now()).replace(" ", "_").replace(".", "_").replace(":", "_")
    return output_dir + "/" + dataset_name + "_" + algorithm_name.replace(" ", "_") + "_" + time + ".csv"
