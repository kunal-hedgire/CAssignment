from django.db import models

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    Gen_Name = models.CharField(max_length=255)
    Gen_Details = models.CharField(max_length=255)
    Gen_slug = models.SlugField(max_length=255)

    def __str__(self):
        return 'Id : {} , Name : {}, Details : {}, Slug : {}'.format(self.id, self.Gen_Name,self.Gen_Details,self.Gen_slug)

    class Meta:
        db_table = 'Genre_Info'

class SubGenre(models.Model):
    id = models.AutoField(primary_key=True)
    Sub_Gen_Name = models.CharField(max_length=255)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    Sub_Gen_Description =models.CharField(max_length=255)
    Sub_Gen_Slug = models.SlugField(max_length=255)

    def __str__(self):
        return 'Id: {}, Name : {}, Genre : {}, Description : {} , Slug : {}'.format(self.id ,self.Sub_Gen_Name,self.genre,self.Sub_Gen_Description, self.Sub_Gen_Slug)


    class Meta:
        db_table='SubGenre_Info'

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    Author_Name = models.CharField(max_length=200)
    subGen = models.ForeignKey(SubGenre, on_delete=models.CASCADE)
    AuthorRating = models.CharField(max_length=200)
    AuthorInfo = models.CharField(max_length=200)

    def __str__(self):
        return 'Id : {}, Name : {}, SubGen : {}, Rating  : {}, Info : {} '.format(self.id,self.Author_Name,self.subGen,self.AuthorRating,self.AuthorInfo)

    class Meta:
        db_table = 'Author_Info'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=4)
    currency = models.CharField(max_length=200)

    def __str__(self):
        return '-------BookInfo---------\n Id : {}, Name :  {}, Author : {}, Cost : {}, Currency : {}'.format(self.id,self.Name,self.author,self.cost,self.currency)


    class Meta:
        db_table = 'Book_Info'

