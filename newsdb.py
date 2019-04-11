#!/usr/bin/env python2

import psycopg2

# Question 1: What are the three most popular articles of all time?
query_articles = """select articles.title, count(*) as views
                    from articles inner join log on log.path
                    like concat('%', articles.slug, '%')
                    where log.status like '%200%' group by
                    articles.title, log.path order by views desc limit 3"""

# Question 2: Who are the most popular article authors of all time?
query_authors = """select authors.name, count(*) as views from articles inner
                    join authors on articles.author = authors.id inner join log
                    on log.path like concat('%', articles.slug, '%') where
                    log.status like '%200%' group
                    by authors.name order by views desc"""

# Question 3: On which day did more than 1% of requests lead to errors?
query_errors = """select * from (
                  select access.day,
                  round(cast((100*errors.hits)
                  as numeric) / cast(access.hits as numeric), 2)
                  as percent from
                  (select date(time)
                  as day, count(*) as hits from log group by day) as access
                  inner join
                  (select date(time) as day, count(*) as hits from log
                  where status like '%404%' group by day) as errors
                  on access.day = errors.day)
                  as total where percent >= 1.0;"""


# Query data from the database, open and close the connection.
def query_conn(sql_request):
    """ Query data from the database, open and close the connection """
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    conn.close()
    return results

# Writing the report
report = open("log-analyzes.txt", "w+")

# Print the top three articles of all time
def top_three_articles():
    top_three_articles = query_conn(query_articles)

    report.write("\nTop 3 articles of all time\n")

    for title, num in top_three_articles:
        report.write("\n  {} -- {} views".format(title, num))

# Print the top authors of all time
def rank_authors():
    rank_authors = query_conn(query_authors)

    report.write("\n\nTop authors of all time\n")

    for name, num in rank_authors:

        report.write("\n  {} -- {} views".format(name, num))

# Print the days in which there were more than 1% bad requests
def over1_error_days():
    over1_error_days = query_conn(query_errors)

    report.write("\n\nDays with more than one percentage of bad requests\n")

    for day, percent in over1_error_days:
        report.write("\n  {} -- {} % errors\n".format(day, percent))


if __name__ == '__main__':
    top_three_articles()
    rank_authors()
    over1_error_days()