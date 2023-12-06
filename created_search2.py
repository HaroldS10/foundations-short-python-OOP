from abc import ABCMeta, abstractmethod
from typing import Callable, Optional, Optional, TypeVar, Tuple, List
from abc import ABCMeta, abstractproperty, abstractmethod
import unittest

T = TypeVar('T')

# Interfaz para obtener el valor de un nodo en el árbol binario
class ValorObtenible(metaclass=ABCMeta):
    @abstractproperty
    def valor(self) -> T:
        """
        Propiedad abstracta para obtener el valor almacenado en el nodo.

        Returns:
            int: El valor almacenado en el nodo.
        """
        pass


# Interfaz para obtener el valor de un nodo en el árbol binario
class PadreObtenible(metaclass=ABCMeta):
    @abstractproperty
    def padre(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al padre del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al padre del nodo actual.
        """
        pass


# Interfaz para obtener los hijos izquierdo y derecho de un nodo en el árbol binario
class HijosObtenibles(metaclass=ABCMeta):
    @abstractproperty
    def izquierda(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al hijo izquierdo del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo izquierdo del nodo actual.
        """
        pass

    @izquierda.setter
    @abstractmethod
    def izquierda(self, value: 'NodoInterface') -> None:
        """
        Propiedad abstracta para establecer el nodo que representa al hijo izquierdo del nodo actual.

        Args:
            value (NodoInterface): El nodo que representa al hijo izquierdo del nodo actual.
        """
        pass

    @abstractproperty
    def derecha(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al hijo derecho del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo derecho del nodo actual.
        """
        pass

    @derecha.setter
    @abstractmethod
    def derecha(self, value: 'NodoInterface') -> None:
        """
        Propiedad abstracta para establecer el nodo que representa al hijo derecho del nodo actual.

        Args:
            value (NodoInterface): El nodo que representa al hijo derecho del nodo actual.
        """
        pass

# Interfaz completa para un nodo en el árbol binario
class NodoInterface(ValorObtenible, HijosObtenibles, PadreObtenible, metaclass=ABCMeta):
    """
    Interfaz que define los métodos que debe implementar cualquier clase que actúe como un nodo en un árbol binario.
    La interfaz incluye métodos para obtener el valor del nodo y sus hijos izquierdo y derecho.
    """
    pass


class Nodo(NodoInterface):
    def __init__(self, valor: T):
      self.__valor = valor
      self.izquierda = None
      self.derecha = None
      self.__padre = None
    
    @property
    def valor(self) -> T:
        return self.__valor
    
    @property
    def izquierda(self) -> 'NodoInterface':
        return self.__izquierda
    
    @izquierda.setter
    def izquierda(self, value: 'NodoInterface') -> None:
        self.__izquierda = value
        if value != None:
            value.__padre = self
        

        
    @property
    def derecha(self) -> 'NodoInterface':
        return self.__derecha
    
    @derecha.setter
    def derecha(self, value: 'NodoInterface') -> None:
        self.__derecha = value
        if value != None:
            value.__padre = self
            
    @property
    def padre(self) -> 'NodoInterface':
        return self.__padre

# Interfaz para operaciones de inserción en el árbol
class OperacionesInsercion(metaclass=ABCMeta):
    @abstractmethod
    def insertar(self, valor: T, proposicion: Callable[[T, T], bool]) -> None:
        pass

    @abstractmethod
    def insertarAll(self, valores: Tuple[T], proposicion: Callable[[T, T], bool]) -> None:
        pass

# Interfaz para operaciones de búsqueda en el árbol
class OperacionesBusqueda(metaclass=ABCMeta):

    @abstractmethod
    def buscar(self, valor: T) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def buscarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def buscarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        pass

# Interfaz para operaciones de eliminación eßßßn el árbol
class OperacionesEliminacion(metaclass=ABCMeta):
    @abstractmethod
    def eliminar(self, valor: T) -> None:
        pass

    @abstractmethod
    def eliminarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def eliminarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        pass

# Interfaz para operaciones de consulta en el árbol
class OperacionesConsulta(metaclass=ABCMeta):
    @abstractmethod
    def obtener_minimo(self, proposicion: Callable[[Optional[NodoInterface]], int]) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def obtener_maximo(self, proposicion: Callable[[Optional[NodoInterface]], int]) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def altura(self) -> int:
        pass

    @abstractmethod
    def es_hoja(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def esta_derecho(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def esta_izquierdo(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def es_raiz(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def es_vacio(self) -> bool:
        pass

    @abstractmethod
    def cantidad_nodos(self) -> int:
        pass

    @abstractmethod
    def recorrido_inorder(self) -> Tuple[T]:
        pass

    @abstractmethod
    def recorrido_preorder(self) -> Tuple[T]:
        pass

    @abstractmethod
    def recorrido_postorder(self) -> Tuple[T]:
        pass

    @abstractproperty
    def root(self) -> Optional[NodoInterface]:
        pass

# Interfaz para operaciones de árbol binario de búsqueda
class ArbolBinarioBusqueda(metaclass=ABCMeta):
    @abstractmethod
    def es_arbol_binario_busqueda(self) -> bool:
        pass

    @abstractmethod
    def obtener_padre(self, valor: T) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def obtener_hermanos(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def nivel_nodo(self, valor: T) -> int:
        pass

    @abstractmethod
    def ancestros(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def cantidad_hojas(self) -> int:
        pass


# Interfaz que combina todas las operaciones de un árbol binario
class Arbol(OperacionesInsercion, OperacionesBusqueda, OperacionesEliminacion, OperacionesConsulta, metaclass=ABCMeta):
    pass


class ArbolBinario(Arbol):
    def __init__(self, raiz=None) -> None:
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz
    
    def insertar(self, valor: T, proposicion: Callable[[T, T], bool]) -> None:
        
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        self._insertar_recursiva(valor, proposicion, self.raiz)
    
    def _insertar_recursiva(self, valor: T, proposicion: Callable[[T, T], bool], nodo_actual: 'NodoInterface') -> None:
        
        if valor == nodo_actual.valor:
            return
        
        if not proposicion(valor, nodo_actual.valor) and nodo_actual.derecha is None:
            nodo_actual.derecha = Nodo(valor)
            return
        
        if proposicion(valor, nodo_actual.valor) and nodo_actual.izquierda is None:
            nodo_actual.izquierda = Nodo(valor)
            return
        
        if not proposicion(valor, nodo_actual.valor): 
            self._insertar_recursiva(valor, proposicion, nodo_actual.derecha)
            return
        
        if proposicion(valor, nodo_actual.valor):
            self._insertar_recursiva(valor, proposicion, nodo_actual.izquierda)
            return
        
    def insertarAll(self, valores: Tuple[T], proposicion: Callable[[T, T], bool]) -> None:
        for value in valores:
            self.insertar(value, proposicion)
    
    def buscar(self, valor: T) -> Optional[NodoInterface]:
        return self._buscar_recursiva(valor, self.__raiz)

    def buscarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self._buscarAll_recursiva(valor, self.__raiz, resultados)
        return tuple(resultados)

    def buscarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self._buscarWhere_recursiva(proposicion, self.__raiz, resultados)
        return tuple(resultados)

    def _buscar_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface]) -> Optional[NodoInterface]:
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual

        if valor < nodo_actual.valor:
            return self._buscar_recursiva(valor, nodo_actual.izquierda)
        
        if valor > nodo_actual.valor:
            return self._buscar_recursiva(valor, nodo_actual.derecha)

    def _buscarAll_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> None:
        if nodo_actual is None:
            return

        if nodo_actual.valor == valor:
            resultados.append(nodo_actual)

        self._buscarAll_recursiva(valor, nodo_actual.izquierda, resultados)
        self._buscarAll_recursiva(valor, nodo_actual.derecha, resultados)

    def _buscarWhere_recursiva(self, proposicion: Callable[[Optional[NodoInterface]], bool], nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> None:
        if nodo_actual is None:
            return

        if proposicion(nodo_actual):
            resultados.append(nodo_actual)

        self._buscarWhere_recursiva(proposicion, nodo_actual.izquierda, resultados)
        self._buscarWhere_recursiva(proposicion, nodo_actual.derecha, resultados)
        
    def eliminar(self, valor: T) -> None:
        self.__raiz = self._eliminar_recursiva(valor, self.__raiz)

    def _eliminar_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface]) -> Optional[NodoInterface]:
        if nodo_actual is None:
            return None

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_recursiva(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursiva(valor, nodo_actual.derecha)
        else:
            # Nodo a eliminar encontrado
            nodo_actual = self._eliminar_nodo(nodo_actual)

        return nodo_actual

    def _eliminar_nodo(self, nodo_actual: NodoInterface) -> Optional[NodoInterface]:
        if nodo_actual.izquierda is None:
            return nodo_actual.derecha
        elif nodo_actual.derecha is None:
            return nodo_actual.izquierda

        # El nodo tiene dos hijos, encontrar el sucesor inmediato
        sucesor = self._encontrar_minimo(nodo_actual.derecha)
        # Crear un nuevo nodo con el valor del sucesor
        nuevo_nodo = Nodo(sucesor.valor)
        nuevo_nodo.izquierda = nodo_actual.izquierda
        nuevo_nodo.derecha = self._eliminar_recursiva(sucesor.valor, nodo_actual.derecha)

        return nuevo_nodo


    def _encontrar_minimo(self, nodo_actual: NodoInterface) -> NodoInterface:
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def eliminarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self.__raiz = self._eliminarAll_recursiva(valor, self.__raiz, resultados)
        return tuple(resultados)

    def _eliminarAll_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> Optional[NodoInterface]:
        if nodo_actual is None:
            return None

        if valor == nodo_actual.valor:
            resultados.append(nodo_actual)
            nodo_actual = self._eliminarAll_recursiva(valor, nodo_actual.izquierda, resultados)
            nodo_actual = self._eliminarAll_recursiva(valor, nodo_actual.derecha, resultados)
        else:
            nodo_actual.izquierda = self._eliminarAll_recursiva(valor, nodo_actual.izquierda, resultados)
            nodo_actual.derecha = self._eliminarAll_recursiva(valor, nodo_actual.derecha, resultados)

        return nodo_actual

    def eliminarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self.__raiz = self._eliminarWhere_recursiva(proposicion, self.__raiz, resultados)
        return tuple(resultados)

    def _eliminarWhere_recursiva(self, proposicion: Callable[[Optional[NodoInterface]], bool], nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> Optional[NodoInterface]:
        if nodo_actual is None:
            return None

        if proposicion(nodo_actual):
            resultados.append(nodo_actual)
            return None  

        nodo_actual.izquierda = self._eliminarWhere_recursiva(proposicion, nodo_actual.izquierda, resultados)
        nodo_actual.derecha = self._eliminarWhere_recursiva(proposicion, nodo_actual.derecha, resultados)

        return nodo_actual
    
    @property
    def root(self):
        return self.__raiz
    
    def obtener_minimo(self, proposicion: Callable[[Optional[NodoInterface]], int]) -> Optional[NodoInterface]:
        pass

    def obtener_maximo(self, proposicion: Callable[[Optional[NodoInterface]], int]) -> Optional[NodoInterface]:
        pass

    def altura(self) -> int:
        pass

    def es_hoja(self, nodo: Optional[NodoInterface]) -> bool:
        pass
    
    def esta_derecho(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    def esta_izquierdo(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    def es_raiz(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    def es_vacio(self) -> bool:
        pass

    def cantidad_nodos(self) -> int:
        
        

    def recorrido_inorder(self, node: 'NodoInterface' = Nodo(None), lista: List = list()) -> Tuple[T]:
        
        if node == None:
            return tuple(lista)
        
        
        if node.valor is None:
            node = self.raiz
        
        
        lista.append(node.valor) 
        # preorder
        self.recorrido_inorder(node.izquierda)
        # inorder
        self.recorrido_inorder(node.derecha)
        # postorder
        
        return tuple(lista)
    
    
    

    def recorrido_preorder(self) -> Tuple[T]:
        pass

    def recorrido_postorder(self) -> Tuple[T]:
        pass


# Clase de prueba para ArbolBinario
class TestArbol():
    def __init__(self):
        nodo1 = Nodo(10)
        self.arbol = ArbolBinario(nodo1)
        self.arbol.insertar(5, lambda x, y : (x < y))
        self.arbol.insertar(4, lambda x, y : (x < y))
        self.arbol.insertar(8, lambda x, y : (x < y))
        self.arbol.insertar(6, lambda x, y : (x < y))
        self.arbol.insertar(9, lambda x, y : (x < y))
        self.arbol.insertar(12, lambda x, y : (x < y))
        self.arbol.insertar(50, lambda x, y : (x < y))
        self.arbol.insertar(60, lambda x, y : (x < y))
        self.arbol.insertar(55, lambda x, y : (x < y))
        self.arbol.insertar(56, lambda x, y : (x < y))

    def test_in_order(self):
        resultado = self.arbol.recorrido_inorder()
        print(resultado)
        

if __name__ == '__main__':
    TestArbol().test_in_order()