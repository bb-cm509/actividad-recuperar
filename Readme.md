# Actividad 2.1 - Errores encontrados

| # | Línea |                            Error encontrado                          | Tipo(Sintaxis/Lógico) |                        Correción                           |
|---|-------|----------------------------------------------------------------------|-----------------------|------------------------------------------------------------|
| 1 |   1   | `Falta importar ABC y abstractmethod`                                |        Lógico         | `from ABC, abstractmethod`                                 |
| 2 |   2   | `Equipo no hereda de ABC`                                            |        Lógico         | `class Equipo(ABC):`                                       |
| 3 |   9   | `Falta @abstractmethod sobre asignar()`                              |        Lógico         | `Agregar @abstractmethod`                                  |
| 4 |   7  | `Falta el':' al final de la función`                                 |       Sintaxis        | `def asignar(self, responsable):`                          |
| 5 | 11 | `No valida si el equipo ya está ocupado`                             |        Lógico         | `Agregar if/else/raise`                                    |
| 6 |   22  | `El mensaje de error no usa f-string ni muestra el código del equipo`|        Lógico         | `Usar f"..." con self.codigo`                              |
| 7 | 27 | `Impresora no escribe el metodo asignar()`                           |        Lógico         | `Agregar el método asignar() completo dentro de Impresora` |