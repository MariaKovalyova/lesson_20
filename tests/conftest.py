from unittest.mock import MagicMock  # Импорт библиотеки для тестов
import pytest

from dao.director import DirectorDAO  # Импорт паттерна для объектов
from dao.model.director import Director  # Импорт класса

from dao.genre import GenreDAO
from dao.model.genre import Genre

from dao.movie import MovieDAO
from dao.model.movie import Movie


@pytest.fixture()
def director_dao():  # Создание схемы для таблицы директор
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='John')
    d2 = Director(id=2, name='Aleks')
    d3 = Director(id=3, name="Kevin")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao


@pytest.fixture()
def genre_dao():  # Создание схемы для таблицы жанры
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='Comedy')
    genre_2 = Genre(id=2, name='Thriller')
    genre_3 = Genre(id=3, name="Drama")

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_dao.create = MagicMock(return_value=genre_3)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()
    return genre_dao


@pytest.fixture()
def movie_dao():  # Создание схемы для таблицы фльимы
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Movie_1', description="description", year=2020)
    movie_2 = Movie(id=2, title='Movie_2', year=1922, rating=10)
    movie_3 = Movie(id=3, title="Movie_3", genre_id=1, trailer="something")

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=movie_3)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    return movie_dao
