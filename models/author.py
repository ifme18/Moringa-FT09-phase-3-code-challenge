from __init__ import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('')
        self._id = cursor.lastrow
        conn.commit()
        conn.close()

   @property
    def id(self):
        return self._id

   @property
    def name(self):
        if not hasattr(self, '_name'):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT name FROM authors WHERE id = ?', (self._id,))
            result = cursor.fetchone()
            if result:
                self._name = result[0]
            else:
                raise ValueError("Name not found in database")
        return self._name 

   @name.setter
    def name(self,value) :
        if not isinstance(value,str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name=value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        ''', (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines    

    def __repr__(self):
        return f'<Author {self.name}>'
