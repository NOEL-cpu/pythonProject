import os
import numpy as np

class Node:
    def __init__(self, path):
        self.name = os.path.basename(path)
        self.fields = self.load_data(os.path.join(path, 'info.txt'))

    def load_data(self, file_path):
        fields = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                print('111', line)
                key, value = line.split(':')
             #   if ((key or value) !=() )
                print('222 ',key,'212 ',value)
                try:
                    fields[key.strip()] = (value.strip())
                except ValueError as exc2:
                    print('333')
        return fields

    def get_field(self, field_name):
        return self.fields.get(field_name, 0)

    def get_data(self):
        print('121', (self.fields.values()))

        print('!!!!!!!!!!!!!!!!!')
        return np.array(list(self.fields.values()))

class NeuralNetwork:
    def __init__(self, input_nodes, hidden_size, output_size, learning_rate=0.1):
        self.input_nodes = input_nodes
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        input_size = len(input_nodes[0].get_data())
        self.weights_input_hidden = np.random.randn(input_size, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feedforward(self):
        print(self.input_nodes)
        print(self)
        try:
           # inputs = np.array([node.get_data() for node in self.input_nodes])
            # Шаг 1: Создание списка данных от каждого узла
            node_data_list = [node.get_data() for node in self.input_nodes]
            print("Шаг 1: Создание списка данных от каждого узла")
            print(node_data_list)

            # Шаг 2: Преобразование списка в массив NumPy
            inputs = np.array(node_data_list)
            print("Шаг 2: Преобразование списка в массив NumPy")
            print(inputs)

        except ValueError as exc3:
            print('После  исключ')
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden)
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)

        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.output_layer_output = self.sigmoid(self.output_layer_input)

        return self.output_layer_output

    def backpropagation(self, expected_output):
        output = self.output_layer_output
        output_error = expected_output - output
        output_delta = output_error * self.sigmoid_derivative(output)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_layer_output)

        inputs = np.array([node.get_data() for node in self.input_nodes])
        self.weights_hidden_output += self.hidden_layer_output.T.dot(output_delta) * self.learning_rate
        self.weights_input_hidden += inputs.T.dot(hidden_delta) * self.learning_rate

    def train(self, training_outputs, epochs=10000):
        for epoch in range(epochs):
            self.feedforward()
            self.backpropagation(training_outputs)

def load_nodes_from_directory(directory_path):
    nodes = []
    index=0
    for root, dirs, files in os.walk(directory_path):
        for dir_name in dirs:
            index += 1
            folder_path = os.path.join(root, dir_name)
            print(index, '  имя папки', dir_name)
            info_file_path = os.path.join(folder_path, 'info.txt')
            if os.path.exists(info_file_path):
                nodes.append(Node(folder_path))
    return nodes

def sort_nodes_by_field(nodes, field_name):
    return sorted(nodes, key=lambda node: node.get_field(field_name), reverse=True)

if __name__ == "__main__":
    directory_path = "C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder"

    # Загрузка узлов из указанной директории
    input_nodes = load_nodes_from_directory(directory_path)

    # Сортировка узлов по значению первого поля (предполагаем, что поле называется 'field1')
    sorted_nodes = sort_nodes_by_field(input_nodes, 'field1')

    # Создание экземпляра класса NeuralNetwork
    nn = NeuralNetwork(input_nodes=sorted_nodes, hidden_size=2, output_size=1)

    # Пример данных для тренировки (исключительно для демонстрации)
    training_outputs = np.array([[0], [1], [1], [0]])

    # Тренировка нейронной сети
    nn.train(training_outputs, epochs=10000)

    # Тестирование нейронной сети
    print("Результаты после тренировки:")
    for node in sorted_nodes:
        print('какой-то результат от нейронной сети')
        print(f"Для {node.name} ->", nn.feedforward())
