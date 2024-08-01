import os
import glob
import duckdb
import argparse

def run_migrations(database, direction):
    conn = duckdb.connect(database=database)
    
    migration_files = sorted(glob.glob(os.path.join("./migrations", '*.'+direction+'.sql')), reverse=direction=='down')

    for file in migration_files:
        with open(file, 'r') as f:
            sql_commands = f.read()

        try:
            conn.execute(sql_commands)
            print(f"Successfully executed {file}")
        except Exception as e:
            print(f"Failed to execute {file}: {e}")
            conn.rollback()
    
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Run database migrations.')
    parser.add_argument('--test', action='store_true', help='Run migrations in test mode')
    parser.add_argument('--prod', action='store_true', help='Run migrations in production mode (persistent database).')

    parser.add_argument('--up', action='store_true', help=').')
    parser.add_argument('--down', action='store_true', help='Run migrations in production mode (persistent database).')

    args = parser.parse_args()

    if args.test and args.prod:
        print("Please specify either --test or --prod, not both.")
        return
    
    if args.up and args.down:
        print("Please specify either --up or --down, not both.")
        return
    
    if args.test:
        database = './db/test.db'
    elif args.prod:
        database = './db/prod.db'  # Specify the path to your persistent database file
    else:
        print("Please specify either --test or --prod.")
        return
    if args.up:
        run_migrations(database, 'up')
    elif args.down:
        run_migrations(database, 'down')
    else:
        print("Please specify either --up or --down.")
        return

if __name__ == "__main__":
    main()
