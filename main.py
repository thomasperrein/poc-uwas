import duckdb

# Connexion à la base de données
con = duckdb.connect("./db/places.db")

# Exécution du fichier SQL pour créer la table
with open('./migrations/20240801153800.up.sql', 'r') as f:
    create_table_sql = f.read()
con.execute(create_table_sql)

# Insertion de données dans la table
con.execute("INSERT INTO places (id, name) VALUES (1, 'Example Place')")

con.table("places").show()

# Exécution du fichier SQL pour supprimer la table
with open('./migrations/20240801153800.down.sql', 'r') as f:
    drop_table_sql = f.read()
con.execute(drop_table_sql)

# Fermeture explicite de la connexion
con.close()
