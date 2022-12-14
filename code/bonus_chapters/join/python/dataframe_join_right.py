% ~/spark-3.2.1/bin/spark-submit dataframe_join_right.py

triplets =  [('alex', 'Ames', 20), ('alex', 'Sunnyvale', 30), ('alex', 'Cupertino', 40), ('mary', 'Ames', 35), ('mary', 'Stanford', 45), ('mary', 'Campbell', 55), ('jeff', 'Ames', 60), ('jeff', 'Sunnyvale', 70), ('jane', 'Austin', 80)]
df.count():  9
df.collect():  [Row(name='alex', city='Ames', age=20), Row(name='alex', city='Sunnyvale', age=30), Row(name='alex', city='Cupertino', age=40), Row(name='mary', city='Ames', age=35), Row(name='mary', city='Stanford', age=45), Row(name='mary', city='Campbell', age=55), Row(name='jeff', city='Ames', age=60), Row(name='jeff', city='Sunnyvale', age=70), Row(name='jane', city='Austin', age=80)]
+----+---------+---+
|name|     city|age|
+----+---------+---+
|alex|     Ames| 20|
|alex|Sunnyvale| 30|
|alex|Cupertino| 40|
|mary|     Ames| 35|
|mary| Stanford| 45|
|mary| Campbell| 55|
|jeff|     Ames| 60|
|jeff|Sunnyvale| 70|
|jane|   Austin| 80|
+----+---------+---+

root
 |-- name: string (nullable = true)
 |-- city: string (nullable = true)
 |-- age: long (nullable = true)

triplets2 =  [('david', 'software'), ('david', 'business'), ('terry', 'coffee'), ('terry', 'hardware'), ('mary', 'marketing'), ('mary', 'sales'), ('jane', 'genomics')]
df2.count():  7
df2.collect():  [Row(name='david', dept='software'), Row(name='david', dept='business'), Row(name='terry', dept='coffee'), Row(name='terry', dept='hardware'), Row(name='mary', dept='marketing'), Row(name='mary', dept='sales'), Row(name='jane', dept='genomics')]
+-----+---------+
| name|     dept|
+-----+---------+
|david| software|
|david| business|
|terry|   coffee|
|terry| hardware|
| mary|marketing|
| mary|    sales|
| jane| genomics|
+-----+---------+

root
 |-- name: string (nullable = true)
 |-- dept: string (nullable = true)

+----+--------+----+-----+---------+
|name|    city| age| name|     dept|
+----+--------+----+-----+---------+
|null|    null|null|david| software|
|null|    null|null|david| business|
|jane|  Austin|  80| jane| genomics|
|mary|    Ames|  35| mary|marketing|
|mary|Stanford|  45| mary|marketing|
|mary|Campbell|  55| mary|marketing|
|mary|    Ames|  35| mary|    sales|
|mary|Stanford|  45| mary|    sales|
|mary|Campbell|  55| mary|    sales|
|null|    null|null|terry|   coffee|
|null|    null|null|terry| hardware|
+----+--------+----+-----+---------+

root
 |-- name: string (nullable = true)
 |-- city: string (nullable = true)
 |-- age: long (nullable = true)
 |-- name: string (nullable = true)
 |-- dept: string (nullable = true)
