# Explicación diagramas


Encontraremos aquí el diagrama de arquitectura y el modelo de datos.


Con relación al modelo de datos, sabemos que hay 3 tipos: el conceptual, el lógico y el físico(Modelo de datosreal).

En primer lugar, el conceptual que es el que nos ayuda a dar una vista empresarial estructurada de los datos necesarios para dar soporte al negocio.
En este caso, lo primordial aquí eran nuestros clientes, Customer, a los que se les asignaría mediante un proceso, un seguro de vida de forma personalizada, Price. Así, identificamos nuestros datos en el negocio.

En segundo lugar, el modelo lógico donde describimos los datos con el mayor detalle posible, sin tener al respecto el cómo serán físicamente implementados en la base de datos.
Es decir, incluimos todas nuestras entidades con sus atributos: Price, el precio a pagar del cliente, que tiene como atributos, la bonificación (dependiendo de la distancia andada se hará un descuento), el recargo (dependiendo de su estado de salud se le cobrará más) y la prima total, el cálculo del precio teniendo en cuenta las variables anteriores.
Por otra parte, en la entidad donde calculamos los kilómetros andados, KmCount, se añaden los atributos biking_distance y walking_distance, dos distancias distintas y un tiempo asociado, timecal. En cuanto a la entidad, Client Coordinates, entidad donde guardamos las coordenadas de los clientes, almacenamos la longitud, la latitud y el método de transporte, entre otros.  Finalmente, en la entidad Customer, nuestro Cliente, le atribuimos todas las caracterísiticas importantes para el cálculo de la prima, desde su edad hasta si ha tenido una patología previa.

En último lugar, el modelo de datos físico donde definimos todos los componentes y servicios de bases de datos lógicas que se requieren para construir una base de datos. Las primary keys de todas nuestra entidades es ClientID que es la forma en la que inequívocamente identificamos a cada persona ya que es único. Además, ClientCoordinates tiene una primary key adicional, createDate, para poder contabilizar el tiempo de los pasos caminados. En cuanto a las relaciones entre las entidades, Clientes y ClientCoordinates es one to many, ya que un cliente tendrá varias coordenadas mientras que ClientCoordinates y Price es many to one, ya que varias coordenadas resultarán en un precio asignado. Por otro lado, la relación entre Clientes y KmCount es many to one, ya que un cliente solo tiene un número de kilómetro asignado mientras que, KmCount y Price, es one to one ya que un sumatorio de km significará un precio único.
