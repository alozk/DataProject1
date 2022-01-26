"""

VARIABLES Y SU PUNTUACIÓN MÁS FAVORABLE:

    EDAD, PUNTOS MÁXIMOS: 5
    PATOLOGÍA PREVIA, PUNTOS MÁXIMOS: 4 (explicar que se considera)
    TENSIÓN ARTERIAL, PUNTOS MÁXIMOS: 4
    KILÓMETROS, PUNTOS MÁXIMOS: 3,5
    % DE GRASA, PUNTOS MÁXIMOS: 3
    NIVEL DE COLESTEROL(total), PUNTOS MÁXIMOS: 3
    FUMADOR, PUNTOS MÁXIMOS: 3
    SEXO, PUNTOS MÁXIMOS: 0,5
    MINUSVALÍA, IF TRUE, FORMULA = NULL [NO ES POSIBLE APLICAR DESCUENTO POR (AL MENOS POR SALUD)]

VALOR VARIABLE EN EL GENERADOR:(valores mínimos-máximos generados)

    EDAD: 18-100?
    PATOLOGÍA PREVIA: True or False
    TENSIÓN ARTERIAL:
        SISTOLICA: 100-200
        DIASTOLICA: 70-130
                    if sistolica <120, diastolica <80 y viceversa
                    if sistolica >120,<129, diastolica <80 y viceversa
                    if sistolica >=130, diastolica >80 y viceversa
                    [es decir, si es normal en una, también en ambas,
                    si tiene en una Hipertension en una, tiene en ambas,
                    si tiene en una crisis hipertensiva, tiene ambas]
    KILÓMETROS: 0-10?
    % DE GRASA: 3%-50%
    NIVEL DE COLESTEROL(total): 150-300
    FUMADOR: True or False
    SEXO: F or M
    MINUSVALÍA: True or False

SISTEMA DE PUNTOS POR VARIABLE:
    EDAD:
        if 18-35, 5 puntos
        if 36-49, 3 puntos
        if 50-65, 1 puntos
    PATOLOGÍA PREVIA:
        if False, 4 puntos
        if True, 0 puntos
    TENSIÓN ARTERIAL:
        SISTOLICA: 100-200
            if <120, 2 puntos
            if >120,<129, 1 puntos
            if >=130, 0 puntos
        DIASTOLICA: 70-130
            if <80, 2 puntos

    KILÓMETROS:
        if edad >18,<35 y hace >8km, 3.5 puntos
        if edad>=36,<49 ya hace >7km 3.5 puntos
        if edad>=50,<65 y hace >5km 3.5 puntos
        if edad >=66 y hace >3km 3.5 puntos
    % DE GRASA:
        if hombre y %grasa >=6,<=17, 3 puntos
        if hombre y %grasa >17,<24, 1 puntos
        if mujer y %grasa >=14,<=24, 3 puntos
        if hombre y %grasa >24,<31, 1 puntos
    
    NIVEL DE COLESTEROL(total):
        if <200, 3 puntos
    FUMADOR:
        if False, 3 puntos

    SEXO:
        if Female, 0.5 puntos

    MINUSVALÍA:
        if False, 0 puntos
        if True, formula = null

"""