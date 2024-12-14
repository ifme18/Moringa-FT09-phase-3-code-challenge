class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @property
    def id(self):
        return self _.id

    @property
    def name(self):
        return self _.name

    @name.setter
    def name(self,value):
        if not isinstance(value, str) or len(value) < 2 or len(value)>16
    self._name= value 


    @propertydef 
    def category(self):
        return self _.category 
    @category.setter
    def category(self,value):
        if not isinstance(value str) or  len(value) == 0
        raise ValueError("ni kubaya hizo values ni za umbwakni")       
    
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        contributors = cursor.fetchall()
        conn.close()
        return contributors

    
    
    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT title FROM articles WHERE magazine_id = ?', (self.id,))
        titles = [row['title'] for row in cursor.fetchall()]
        conn.close()
        return titles if titles else None

   
    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT authors.*, COUNT(articles.id) as article_count FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
        ''', (self.id,))
       
        authors = cursor.fetchall()
        conn.close()
        
        return authors if authors else None

    def __repr__(self):
        return f'<Magazine {self.name}>'
