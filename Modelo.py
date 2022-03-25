class Modelo:
    @property
    def posicion_x(self):
        return self._posicion_x
    @posicion_x.setter
    def posicion_x(self,posicion_x):
        self._posicion_x = posicion_x
    
    @property
    def posicion_y(self):
        return self._posicion_y
    @posicion_y.setter
    def posicion_y(self,posicion_y):
        self._posicion_y = posicion_y

    @property
    def posicion_z(self):
        return self._posicion_z
    @posicion_z.setter
    def posicion_z(self,posicion_z):
        self._posicion_z = posicion_z

    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad = velocidad

    @property
    def posicion(self):
        return self._posicion
    @posicion.setter
    def posicion(self,posicion):
        self._posicion = posicion
        
    @property
    def angulo(self):
        return self._angulo
    @angulo.setter
    def angulo(self,angulo):
        self._angulo = angulo
    
    @property
    def velocidad_rotacion(self):
        return self._velocidad_rotacion
    @velocidad_rotacion.setter
    def velocidad_rotacion(self,velocidad_rotacion):
        self._velocidad_rotacion = velocidad_rotacion
    
    @property
    def tiempo_anterior(self):
        return self._tiempo_anterior
    @tiempo_anterior.setter
    def tiempo_anterior(self,tiempo_anterior):
        self._tiempo_anterior = tiempo_anterior

    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self,direccion):
        self._direccion = direccion

    def __init__(self, posicion_x = -0.7, posicion_y = 0.7, posicion_z = 0.0, velocidad = 0.003, direccion = 0, tiempo_anterior = 0.0):
        self._posicion_x = posicion_x
        self._posicion_y = posicion_y
        self._posicion_z = posicion_z
        self._velocidad = velocidad
        self._direccion = direccion
        self._tiempo_anterior = tiempo_anterior
    
    def colisionando(self, modelo):
        assert isinstance(modelo,Modelo)
        self.colisionando = False


        