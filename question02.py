import numpy as np


def main():
    random_vector = np.random.uniform(1, 20, 20)

    reshaped_array = random_vector.reshape(4, 5)

    reshaped_array[np.arange(len(reshaped_array)), np.argmax(reshaped_array, axis=1)] = 0

    print("Original Array:")
    print(random_vector)
    print("\nReshaped Array:")
    print(reshaped_array)


if __name__ == '__main__':
    main()
