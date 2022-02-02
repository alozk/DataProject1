****ACTUALIZADO****☝️☝️Leer el documento Word de variables, esta tarde remato el análisis del dataset(ipynb)

Bueno compañeros, el objetivo de este dataset es dar explicaciones en la medida de lo posible de el porqué de la elección de las variables usadas. Lo malo es de este dataset es que **no me ha permitido el uso de scatterplot dado que solo he usado como cuantitativa la edad**. Los valores de la presión arterial (sistólica y diastólica) tenían números negativos, el dataset es estadounidense y me ha pasado alguna vez que sus mediciones cambian respecto a como las conocemos aquí. **El dataset no parece tener fuente pero parece el más fiable**, entre otras cosas por que aparte de tener sentido, podemos acceder al mismo LinkedIn de la propietaria. El punto bueno es que el **tamaño muestral es de 70.000**. También comentar que ha hecho falta crear desde Python una columna nueva con la edad en años puesto que el dataset solo la proporcionaba en días.

**Para justificar las variables habían dos caminos: sacar de estudios ya realizados las conclusiones a base de texto desde internet o, intentar explicar a base de lo aprendido con Estadística con Python.**

Encontrar un dataset que fuese útil ha sido muy complicado, he elegido uno que al menos tuvieran unas cuantas variables y las he relacionado con la edad, nuestra variable predicha puesto que es la que directamente tiene que ver con la esperanza de vida. **Recordemos que al final una aseguradora lo que quiere es poner precio acorde a la esperanza de cada individuo y lo hace con el uso de las variables que hemos empleado en nuestro datagenerator.py.**

Soy consciente de que ahora mismo falta pulir el documento ipynb.
La intención mía es usar **la variable predicha (edad) con el colesterol, actividad física y problemas cardíacos** (predictoras, todas por desgracia son cualitativas), lo cual creo que si está todo correcto.

**A revisar** está la segunda parte, en la que ya no uso la edad junto con otras variables, sino que intento no solo justificar porque las mujeres pagan menos sacando de internet que su esperanza de vida es mayor, sino que muestro **que los hombres fuman y beben más**.
