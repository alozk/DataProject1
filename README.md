![MicraLogo](https://github.com/micra-consulting-sl/Micra-Consulting/blob/main/LOGO/MicraLogo.jpg)

# MICRA Consulting

Somos una startup especializada en proporcionar soluciones innovadoras a través de herramientas Big Data.

Minimizaremos tus problemas; maximizaremos tus beneficios.

## [](https://github.com/micraconsulting/micraconsulting#nuestros-valores-)Nuestros valores :

-   Mejora continua
-   Impacto positivo
-   Calidad humana

## [](https://github.com/micraconsulting/micraconsulting#c%C3%B3mo-funcionamos)¿Cómo funcionamos?

-   #### [](https://github.com/micraconsulting/micraconsulting#consulting)Consulting:
    

Definimos la mejor estrategia personalizada a tu negocio con el objetivo de la optimización de tus ganancias.

-   #### [](https://github.com/micraconsulting/micraconsulting#integraci%C3%B3n)Integración:
    

Desarrollamos un software individualizado con la correspondiente integración al negocio.

-   #### [](https://github.com/micraconsulting/micraconsulting#an%C3%A1lisis-y-datos)Análisis y datos:
    

Descubrimos patrones y correlaciones a través del análisis de datos para implementar mejoras, conocer el comportamiento de los usuarios o adaptar la estrategia.

## [](https://github.com/micraconsulting/micraconsulting#conoce-a-nuestro-equipo)

Conoce a nuestro equipo

En nuestro equipo multidisciplinar destacan el compromiso, la innovación y la honestidad.

Está compuesto por:

**Marta Castillo**  [![Linkedin Badge](https://img.shields.io/badge/-Marta-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chiquillo/)](https://www.linkedin.com/in/marta-castillo-garc%C3%ADa-041bb169/)

**Álvaro Chiquillo**  [![Linkedin Badge](https://img.shields.io/badge/-Alvaro-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chiquillo/)](https://www.linkedin.com/in/chiquillo/)

**Jose Manuel García**  [![Linkedin Badge](https://img.shields.io/badge/-JoseManuel-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chiquillo/)](https://www.linkedin.com/in/jogacu/)

**Ismail Kinani**  [![Linkedin Badge](https://img.shields.io/badge/-Ismail-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chiquillo/)](https://www.linkedin.com/in/ismail-kinani-666472223/)

**Rafa Pérez**  [![Linkedin Badge](https://img.shields.io/badge/-Rafa-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chiquillo/)](https://www.linkedin.com/in/rafa-perez-solans/)

Contacta con nosotros:

📧 micraconsulting@outloook.es

# Setup

## Iniciar Kafka

Acceder a la carpeta KAFKA_datagenerator y levantar el contenedor.

1) Levantar el contenedor: docker-compose up -d
2) Crear topic:
   - docker exec -it kafka /bin/sh
   - cd kafka_<version>
   - ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 -- partitions 1 --topic <name_topic>

Una vez levantado el contenedor y creado el topic de Kafka, se debe asegurar que el nombre del topic coincida con el que hay en el consumer.py

## Base de datos MySQL

Para levantar la imagen de docker:

docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret -d mysql
    - User: root
    - Password: secret

Instalar la siguiente libreria de python: 

   - pip install mysql-connector

Para poder visualizar la base de datos:

- Instalar DBeaver (o cualquier otro visualizador) e introducir :
  - User: root
  - Password: secret
  - Port: 3306
  - DataBase: *empty*

Asegurarse que en el archivo consumer.py el port, user, password coincidan.
