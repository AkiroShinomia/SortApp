import tkinter as tk
import time


class Node:
    #Класс узла бинарного дерева. 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    #Класс бинарного дерева. 
    def __init__(self):
        self.root = None

    def insert(self, value):
        #Метод для вставки значения в бинарное дерево.
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        #Рекурсивный метод для вставки значения в бинарное дерево. 
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)

    def in_order_traversal(self):
        #Метод для обхода бинарного дерева в порядке сортировки. 
        elements = []
        self._in_order_traversal_recursively(self.root, elements)
        return elements

    def _in_order_traversal_recursively(self, node, elements):
        #Рекурсивный метод для обхода бинарного дерева в порядке сортировки. 
        if node:
            self._in_order_traversal_recursively(node.left, elements)
            elements.append(node.value)
            self._in_order_traversal_recursively(node.right, elements)


class SortingApp:
    #Класс графического приложения для сортировки чисел. 
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting App")

        # Создаем и размещаем элементы интерфейса
        self.input_label = tk.Label(root, text="Введите последовательность чисел (через запятую):")
        self.input_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.sort_options = ["Сортировка по возрастанию", "Сортировка по убыванию", "Сортировка бинарным деревом"]
        self.sort_var = tk.StringVar(root)
        self.sort_var.set(self.sort_options[0])

        self.sort_label = tk.Label(root, text="Выберите метод сортировки:")
        self.sort_label.pack()

        self.sort_menu = tk.OptionMenu(root, self.sort_var, *self.sort_options)
        self.sort_menu.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_sorting)
        self.start_button.pack()

        self.output_label = tk.Label(root, text="Результат сортировки:")
        self.output_label.pack()

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack()

    def start_sorting(self):
        """Метод для начала сортировки."""
        try:
            # Получаем введенную последовательность чисел
            input_sequence = self.input_entry.get().strip()
            numbers = [float(x.strip()) for x in input_sequence.split(',')]

            # Замеряем время начала сортировки
            start_time = time.time()

            # Выполняем сортировку в зависимости от выбора пользователя
            if self.sort_var.get() == self.sort_options[0]:
                numbers.sort()
            elif self.sort_var.get() == self.sort_options[1]:
                numbers.sort(reverse=True)
            else:
                # Создаем бинарное дерево и вставляем элементы
                tree = BinaryTree()
                for num in numbers:
                    tree.insert(num)
                
                # Получаем отсортированный список из бинарного дерева
                numbers = tree.in_order_traversal()

            # Замеряем время окончания сортировки и вычисляем время выполнения
            end_time = time.time()
            duration = end_time - start_time

            # Очищаем текстовое поле вывода и выводим результат сортировки и время выполнения
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Отсортированная последовательность: {numbers}\n")
            self.output_text.insert(tk.END, f"Время выполнения сортировки: {duration:.6f} секунд")

        except ValueError:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Ошибка: Введите корректную последовательность чисел.")
        except Exception as e:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Ошибка: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
