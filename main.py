import duckdb

con = duckdb.connect("./db/test.db")

con.table("places").show()

con.close()
