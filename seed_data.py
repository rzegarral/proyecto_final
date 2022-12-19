"""
from ejemplo.models import Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745",numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Av. Central 125",numero_pasaporte=892126).save()
Familiar(nombre="Samuel", direccion="Calle las Peras 98",numero_pasaporte=232365).save()
Familiar(nombre="Florencia", direccion="Jiron Union 701",numero_pasaporte=951951).save()
Familiar(nombre="Gerardo", direccion="Rio Parana 650",numero_pasaporte=354612).save()
Familiar(nombre="Nazario", direccion="Rio Parana 745",numero_pasaporte=659487).save()
Familiar(nombre="Paola", direccion="Rio Parana 745",numero_pasaporte=787532).save()
Familiar(nombre="Walter", direccion="Calle 2 de Junio 125",numero_pasaporte=654189).save()
print("Se cargo con éxito los usuarios de pruebas")

from ejemplo.models import Amigos
Amigos(nombre="Rosario", direccion="Rio Parana 745",edad=23, pais="Perú").save()
Amigos(nombre="Alberto", direccion="Av. Central 125",edad=38, pais="Colombia").save()
Amigos(nombre="Samuel", direccion="Calle las Peras 98",edad=29, pais="Ecuador").save()
Amigos(nombre="Florencia", direccion="Jiron Union 701",edad=41, pais="Chile").save()
Amigos(nombre="Gerardo", direccion="Rio Parana 650",edad=33, pais="Argentina").save()
Amigos(nombre="Nazario", direccion="Rio Parana 745",edad=27, pais="Brasil").save()
Amigos(nombre="Paola", direccion="Rio Parana 745",edad=25, pais="Bolivia").save()
Amigos(nombre="Walter", direccion="Calle 2 de Junio 125",edad=38, pais="Venezuela").save()
print("Se cargo con éxito los Amigos de prueba")

"""
from ejemplo.models import Carros
Carros(marca="Nissan", origen="Japón",ano=2018, valor=15000).save()
Carros(marca="Fiat", origen="Italia",ano=2020, valor=20000).save()
Carros(marca="Subaru", origen="Corea",ano=2015, valor=21500).save()
Carros(marca="Mercedes", origen="Alemania",ano=2011, valor=19855).save()
print("Se cargo con éxito los Carros de prueba")

from ejemplo.models import Escuelas
Escuelas(nombre="Isaac Newton", direccion="Rio Parana 745",curso="",tiempo_mes=23, costo_mes=850).save()
Escuelas(nombre="Albert Eisntein", direccion="Av. Central 125",curso="",tiempo_mes=38, costo_mes=975).save()
Escuelas(nombre="World Sapiens", direccion="Calle las Peras 98",curso="",tiempo_mes=29, costo_mes=789).save()
print("Se cargo con éxito las Escuelas de prueba")
