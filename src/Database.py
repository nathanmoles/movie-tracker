import MySQLdb

class Database:
    db = None
    cur = None

    #constructor that connects to the database and sets it up
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                     user="admin",
                     passwd="angle_4L",
                     db="MovieTracker")

        self.cur = self.db.cursor()
        self.deleteTables()
        self.createTables()

    #decunstructor that closes the connection to the database
    def __del__(self):
        self.db.close()
    
    #creates all tables in the database
    def createTables(self):
        create_statement = """ 
            CREATE TABLE IF NOT EXISTS User(
                username varchar(16),
                firstname varchar(16),
                lastname varchar(16),
                PRIMARY KEY (username)
            );
            ALTER TABLE User AUTO_INCREMENT = 1;
            CREATE TABLE IF NOT EXISTS Movie(
                imdbID int,
                name varchar(16),
                primaryGenre varchar(16),
                secondaryGenre varchar(16),
                PRIMARY KEY (imdbID)
            );
            ALTER TABLE Movie AUTO_INCREMENT = 1;
            CREATE TABLE IF NOT EXISTS UserMovie(
                username varchar(16),
                movieID int,
                FOREIGN KEY (username) REFERENCES User(username),
                FOREIGN KEY (movieID) REFERENCES Movie(imdbID)
            );"""
        self.cur.execute(create_statement)

    #drop all tables in the database
    def deleteTables(self):
        delete_statement = """
            DROP TABLE IF EXISTS UserMovie;
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS Movie;"""

        self.cur.execute(delete_statement)

    #executes and commits a given sql statement
    def exe(self, statement):
        self.cur.execute(statement)
        self.cur.execute("COMMIT;")