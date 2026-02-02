# Database Transaction Context

class DatabaseTransaction:
    def __init__(self, connection):
        self.connection = connection
    
    def __enter__(self):
        print("Transaction started")
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Error Occured → ROLLBACK")
            self.connection.rollback()
        else:
            print("No error → COMMIT")
            self.connection.commit()


class FakeDB:
    def commit(self):
        print("DB COMMIT")

    def rollback(self):
        print("DB ROLLBACK")


db = FakeDB()

with DatabaseTransaction(db):
    print("Running queried")
    x = 10/0