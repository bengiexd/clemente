clemente
========

Proyecto Clemente

software para poder manipular plaquitas del proyecto icaro remotamente

explicacion breve del codigo
paquete gui se maneja toda la parte de la interfaz grafica
  paquete "UI Pyside" estan los *.ui con sys respectivos equivalente en python
    los *.ui estan diseñados con qt designer
    los *.py fueron creados usados la herramiente pyside-uic 
    la libreria usada para la interfaz es Pyside
  paquete controller estan los contraloderes de toda la interfaz incluyendo el main principal
  paquete media estan los iconos e logos.png

paquete "server_json_rpc" esta el servidor que usa la libreria cherrepy-json-rpc "cpjsonrpcserver"
  modulo server
  modulo solver resolver las peticiones y enviarselas a la placa icaro
  
paquete "client_json_rpc" esta el cliente 
  modulo client encargado de enviar la informacion codificada en json por POST
  
paquete "doc" donde se incluira toda la documentacion del software clemente
  
los demas paquetes son de versiones anteriores
  paquete server trae modulos de un servidor con sockets multihilo
  paquete clien trae modulos de un cliente con sockets
  
  paquete server_rest es un servidor con servicios rest, hace uso de la libreria cherrypy
  paquete client_rest es un cliente de sercicios rest
  
