import matplotlib.pyplot as plt
import os

FILETYPE = "jpg"

def set_axis():
    axis = plt.gca()
    axis.set_xlim([0.5, 1])
    axis.set_ylim([0.5, 1])

def plot(precision, recall, values):
    assert len(precision) == len(recall)
    assert len(recall) == len(values)

    plt.scatter(precision, recall)
    plt.plot(precision, recall)

    for idx in range(len(values)):
        plt.annotate(values[idx], (precision[idx], recall[idx]), textcoords="data")

    plt.grid()

def set_labels():
    plt.ylabel("Precision")
    plt.xlabel("Recall")

def set_axis_and_labels():
    set_labels()
    set_axis()

def set_legend(name):
    if type(name) == str:
        plt.legend([name], loc="lower right")
    elif type(name) == list:
        plt.legend(name, loc="lower right")
    else:
        raise Exception("Unknown type to legend")

def save_and_clear(filename, legend_name):
    set_legend(legend_name)
    plt.savefig(filename + "." + FILETYPE)
    plt.clf()

def make_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        pass

def make_words_quantity_chart():
    prefix = "word_quantity_charts"
    make_dir(prefix)

    datapoints = [5, 10, 15]
    derbin_x = [0.788, 0.887, 0.711]
    derbin_y = [0.677, 0.799, 0.655]

    malgenome_x = [0.794, 0.722, 0.712]
    malgenome_y = [0.699, 0.621, 0.732]

    aagm_x = [0.774, 0.662, 0.798]
    aagm_y = [0.668, 0.678, 0.776]

    set_axis_and_labels()
    plot(derbin_x, derbin_y , datapoints)
    save_and_clear(prefix + "/Drebin", "Drebin")

    set_axis_and_labels()
    plot(malgenome_x, malgenome_y, datapoints)
    save_and_clear(prefix + "/Malgenome", "Malgenome")
    
    set_axis_and_labels()
    plot(aagm_x, aagm_y , datapoints)
    save_and_clear(prefix + "/AAGM", "AAGM")

    set_axis_and_labels()
    plot(derbin_x, derbin_y, datapoints)
    plot(malgenome_x, malgenome_y, datapoints)
    plot(aagm_x, aagm_y, datapoints)
    set_legend(["Derbin", "Malgenome", "AAGM"])
    plt.savefig(prefix + "/Aggregate." + FILETYPE)
    plt.clf()


def make_topic_quantity_chart():
    prefix = "topic_quantity_charts"
    make_dir(prefix)

    datapoints = [10, 25, 45]
    derbin_x = [0.987, 0.956, 0.947]
    derbin_y = [0.969, 0.945, 0.823]

    malgenome_x = [0.981, 0.988, 0.988]
    malgenome_y = [0.798, 0.955, 0.91]

    aagm_x = [0.948, 0.961, 0.988]
    aagm_y = [0.818, 0.952, 0.946]

    set_axis_and_labels()
    plot(derbin_x, derbin_y, datapoints)
    save_and_clear(prefix + "/Drebin", "Drebin")

    set_axis_and_labels()
    plot(malgenome_x, malgenome_y , datapoints)
    save_and_clear(prefix + "/Malgenome", "Malgenome")
    
    set_axis_and_labels()
    plot(aagm_x, aagm_y, datapoints)
    save_and_clear(prefix + "/AAGM", "AAGM")

    set_axis_and_labels()
    plot(derbin_x, derbin_y, datapoints)
    plot(malgenome_x, malgenome_y, datapoints)
    plot(aagm_x, aagm_y, datapoints)
    set_legend(["Derbin", "Malgenome", "AAGM"])
    plt.savefig(prefix + "/Aggregate." + FILETYPE)
    plt.clf()

def main():
    make_words_quantity_chart()
    make_topic_quantity_chart()
    
if __name__ == "__main__":
    main()

