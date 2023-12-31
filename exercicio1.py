#!/usr/bin/python
# -*- coding: utf-8 -*

class OutOfBoundsException(Exception):
    """
    Exceção para indicar que houve uma tentativa de acesso fora dos limites permitidos.
    """

    def __init__(self, message="Out of bounds"):
        super().__init__(message)


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
        """
        self._head = None  # Apontador para o nó cabeça (primeiro)
        self._tail = None  # Apontador para o nó filho (ultimo)
        self._len = 0  # contador

    def __len__(self):
        return self._len

    @property
    def head(self):
        """
        Esta propriedade deve retornar o valor do primeiro nó da lista ligada
        """
        if self._head:
            return self._head.value
        else:
            return None

    @property
    def tail(self):
        """
        Esta propriedade deve retornar o valor do último nó da lista ligada
        """
        if self._tail:
            return self._tail.value
        else:
            return None

    def append(self, value):
        """
        Esta função deve inserir um novo nó no FINAL da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - append(0) - [1, 2, 3, 0]
        """
        new_node = LinkedListNode(value)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._len += 1

    def insert(self, value):
        """
        Esta função deve inserir um novo nó no INICIO da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - insert(0) - [0, 1, 2, 3]
        """
        new_node = LinkedListNode(value)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._len += 1

    def removeFirst(self):
        """
        Esta função deve remover o primeiro elemento da lista e retornar o seu valor.
        Após a execução, a lista ligada deve ter um elemento a menos.
        """
        if not self._head:
            raise OutOfBoundsException("List is empty")

        value = self._head.value
        self._head = self._head.next
        self._len -= 1

        if not self._head:
            self._tail = None

        return value

    def getValueAt(self, index):
        """
        Esta função deve retornar o valor de um nó na posição definida por INDEX.
        Se o index for maior do que o tamanho da lista, retornar OutOfBoundsException
        """
        if index < 0 or index >= self._len:
            raise OutOfBoundsException("Index out of bounds")

        current_node = self._head
        for i in range(index):
            current_node = current_node.next

        return current_node.value

    def toList(self):
        """
        Esta função retornar uma representação em forma de vetor ([1, 2, 3....])
        da lista ligada
        """
        result = []
        current_node = self._head
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next

        return result


if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    ll = LinkedList()
    assert (ll.head is None)
    assert (ll.tail is None)
    assert (ll.toList() == [])
    ll.append(1)
    assert (ll.head == 1)
    assert (ll.tail == 1)
    assert (len(ll) == 1)
    assert (ll.toList() == [1])
    ll.append(2)
    assert (ll.head == 1)
    assert (ll.tail == 2)
    assert (len(ll) == 2)
    assert (ll.toList() == [1, 2])
    ll.append(3)
    assert (ll.head == 1)
    assert (ll.tail == 3)
    assert (len(ll) == 3)
    assert (ll.toList() == [1, 2, 3])
    ll.insert(0)
    assert (ll.head == 0)
    assert (ll.tail == 3)
    assert (len(ll) == 4)
    assert (ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert (ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert (v == -1)
    assert (ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert (v == 0)
    assert (ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert (v == 1)
    assert (ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert (v == 2)
    assert (ll.toList() == [3])
    v = ll.removeFirst()
    assert (v == 3)
    assert (ll.toList() == [])
    assert (len(ll) == 0)
    print("100%")
