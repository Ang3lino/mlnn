
import random
import numpy as np


def plot_samples(x: np.array, y: np.array, n_samples: int) -> None:
    indexes = set()
    b = len(x)
    while len(indexes) < n_samples:
        indexes.add(random.randint(0, b - 1))
    for i in indexes:
        x_i, y_i = X[i], y[i]
        plot_mat(x_i, y_i)


def classify_using_dataset(i: int, classifiers: []) -> None:
    X, y = get_processed_data(i)  # load the dataset from the subdir i
    instances_counter = Counter(y)  # count the amount of instances per class
    display(instances_counter) 
    
    # preprocessing
    X_hu = dimensionality_reduction(X)  # Transform the feature vector to a list of 7 elements
    X_train, X_test, y_train, y_test = train_test_split(
            X_hu, y, test_size=0.33, random_state=42)

    for clf in classifiers:
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        display(accuracy_score(y_test, y_pred))


def plot_samples(X: np.array, indexes={1,2,3,4}) -> None:
    indexes = set()
    while len(indexes) < 4:
        indexes.add(random.randint(0, X.shape(0)))
    fig, axes = plt.subplots(2, 2)
    m, n = axes.shape
    for i in range(m):
        for j in range(n):
            x_i = X[indexes.pop()]
            u, v = col_j(x_i, 0), col_j(x_i, 1)
            axes[i,j].scatter(u, v, s=3)
    fig.show()
