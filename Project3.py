#! /usr/bin/env python

import psycopg2

DBNAME = "news"

query1 = """select title, count(*) from articles join log
        on path like concat('/article/%',slug)
        group by title order by count(*) desc limit 3;"""

query2 = """select name, count(*) from authors join articles
        on authors.id = articles.author join log
        on path like concat('/article/%',slug)
        group by name order by count(*) desc;"""

query3 = """select total.date, cast((cast(errors.er as decimal)/total.er)*100 as
          decimal(5,2))from (select date_trunc('day',time) as date, count(*)
          as er from log where status like '404%' group by date) as errors join
          (select date_trunc('day',time) as date, count(*) as er from log
          group by date) as total on total.date = errors.date
          where ((cast(errors.er as decimal)/total.er)*100)>1 order by
          cast((cast(errors.er as decimal)/total.er)*100 as decimal(5,2))
          desc;"""


def exe_q(q):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q)
    res = c.fetchall()
    db.close()
    return res


def answer(comd):
    result = exe_q(comd)
    for a in result:
        print('   > "' + a[0] + '"  --  ' + str(a[1]) + " views")


def error_perc(comd):
    result = exe_q(comd)
    for a in result:
        d = a[0].strftime('%b %d, %Y')
        errors = str(a[1]) + "%" + " errors"
        print("   > " + d + "  --  " + errors)

print("1. What are the most popular three articles of all time?")
answer(query1)

print("\n2. Who are the most popular article authors of all time?")
answer(query2)

print("\n3. On which days did more than 1% of requests lead to errors?")
error_perc(query3)
