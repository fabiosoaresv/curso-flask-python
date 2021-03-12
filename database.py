import psycopg2

def postgres_test():
  try:
    con = psycopg2.connect(host='localhost', database='api_python', user='postgres', password='123123')
    con.close()
    return print(True)
  except:
    return print(False)

postgres_test()
