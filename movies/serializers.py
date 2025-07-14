from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializer import ActorSerializer

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self,value):#a def tem que comecar com validate_
        if value.year<1900 :
            raise serializers.ValidationError('A data de lançamento deve ser superior a 1990')
        return value
    
    def validate_resume(self,value):#a def tem que comecar com validate_
        if len(value) > 200 :
            raise serializers.ValidationError('Maximo 200 caracteres.')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):

    genre = GenreSerializer()
    actors = ActorSerializer(many=True) 
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self,obj):#tem que comecar com get_
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate,1)
        return None
        # reviews = obj.reviews.all()
        # if reviews :
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews =+ review.stars
        #     reviews_count = reviews.count()
        #     return round(sum_reviews / reviews_count,1)
        # return None
