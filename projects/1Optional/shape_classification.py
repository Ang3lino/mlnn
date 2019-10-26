
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


x_i = X[0]
u, v = col_j(x_i, 0), col_j(x_i, 1)
plt.scatter(u, v, s=2)

fig, axes = plt.subplots(1, 4)
axes[0, 0].scatter(u, v, s=2)
axes[0, 1].scatter(u, v, s=2)
axes[0, 2].scatter(u, v, s=2)
axes[0, 3].scatter(u, v, s=2)
