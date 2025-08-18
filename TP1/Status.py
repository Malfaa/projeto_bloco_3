from enum import Enum

class Status(Enum):
    PENDENTE = "Pendente"
    DISPENSADA = "Dispensada"
    VENCIDA = "Vencida"
    CANCELADA = "Cancelada"