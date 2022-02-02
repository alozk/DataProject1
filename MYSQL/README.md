Para levantar la imagen de docker:

docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret -d mysql
    - User: root
    - Password: secret

Instalar la siguiente libreria de python: 
   - pip install mysql-connector

Para poder visualizar la base de datos:

- Instalar DBeaver e introducir :
  - User: root
  - Password: secret
  - Port: 3306
  - DataBase: *empty*