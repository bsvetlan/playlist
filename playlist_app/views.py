from collections import namedtuple

from django.db import connection
from django.shortcuts import render


# Create your views here.
def best_executers(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "select \"Executor\".\"Name\", count(*) as s from \"Reward\"  join \"Song\" on \"Reward\".\"SongId\" =\"Song\".\"SongId\" join \"SongExecutor\" on \"SongExecutor\".\"SongId\" =\"Song\".\"SongId\" join \"Executor\" on \"SongExecutor\".\"ExecutorId\" = \"Executor\".\"ExecutorId\" group by \"Executor\".\"Name\" order by s DESC limit 10;",
            [])
        columns = [col[0] for col in cursor.description]
        row = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        print(row)

    return render(request, 'playlist_app/best_executers.html', {'result': row})


def ganre(request):
    with connection.cursor() as cursor:
        if request.method == 'POST':
            year = str(request.POST.get('date')) + '-01-01'
            cursor.execute(
            "select \"Genre\", count(*) from \"Song\" where \"ReleaseYear\" = %s group by \"Genre\";", [year])
            columns = [col[0] for col in cursor.description]
            row = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
            return render(request, 'playlist_app/ganre.html', {'result': row})
        else:
            return render(request, 'playlist_app/ganre.html', {})


def album(request):
    with connection.cursor() as cursor:
        if request.method == 'POST':
            ganres = ""
            for item in (request.POST.get('ganre')).split(', '):
                ganres += "'" + item + "', "
            ganres = "'жанр 1', 'жанр 3', 'жанр 4'"
            sql = "select \"Album\".\"Name\", AVG(\"Rating\") from \"Song\" join \"Album\" on \"Song\".\"AlbumId\"=\"Album\".\"AlbumId\" where \"Song\".\"AlbumId\" IS NOT NULL AND \"Genre\" in ( %s ) group by \"Album\".\"Name\" limit 1;" % (ganres)
            cursor.execute(sql, [])
            columns = [col[0] for col in cursor.description]
            row = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return render(request, 'playlist_app/album.html', {'result': row})
        else:
            return render(request, 'playlist_app/album.html', {})


def execute(request):
    with connection.cursor() as cursor:
        if request.method == 'POST':
            year1 = str(request.POST.get('dateStart')) + '-01-01'
            year2 = str(request.POST.get('dateEnd')) + '-01-01'
            cursor.execute(
                "select \"Executor\".\"Name\" as s from \"Album\"  join \"Song\" on \"Album\".\"AlbumId\" =\"Song\".\"SongId\"  join \"SongExecutor\" on \"SongExecutor\".\"SongId\" =\"Song\".\"SongId\" join \"Executor\" on \"SongExecutor\".\"ExecutorId\" = \"Executor\".\"ExecutorId\" where \"Album\".\"CreationDate\" > %s AND \"Album\".\"CreationDate\" < %s order by \"Executor\".\"Name\"; ", [year1, year2])
            columns = [col[0] for col in cursor.description]
            row = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return render(request, 'playlist_app/execute.html', {'result': row})
        else:
            return render(request, 'playlist_app/execute.html', {})
