from db import get_connection
try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call buscar_Alumnos()')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()


except Exception as ex:
    print(ex)
    pass

try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call buscar_alumno(%s)',(10))
        resultset=cursor.fetchall()
        print(resultset)
    connection.close()


except Exception as ex:
    print(ex)
    pass

try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_alumno(%s,%s,%s)',("nombre","apellidos","correo"))
        connection.commit()
        connection.close()

    connection.close()


except Exception as ex:
    print(ex)
    pass