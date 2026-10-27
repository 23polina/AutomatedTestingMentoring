from sqlalchemy.orm import sessionmaker

from create_table import engine, Film

Session = sessionmaker(bind=engine)

def add_film(film_title, director, release_year):
    with Session() as session:
        new_film = Film(title=film_title, director=director, release_year=release_year)
        session.add(new_film)
        session.commit()
        print("Film is added")


def edit_film(film_id, new_film_title=None, new_director=None, new_release_year=None):
    with Session() as session:
        film = session.get(Film, film_id)
        if not film:
            print("No film found")
        else:
            if new_film_title is not None:
                film.title = new_film_title
            if new_director is not None:
                film.director = new_director
            if new_release_year is not None:
                film.release_year = new_release_year
            session.commit()
            print("Film updated")


def print_data_from_table():
    with Session() as session:
        films = session.query(Film).all()
        if not films:
            print("Films table is empty")
        else:
            for film in films:
                print(film.title, film.director, film.release_year)


def delete_all_table_data():
    with Session() as session:
        session.query(Film).delete()
        session.commit()
        print("All data deleted")


if __name__ == "__main__":
    add_film("The Shawshank Redemption", "Frank Darabont", 1996)
    add_film("Inception", "Christopher Nolan", 2010)
    add_film("Pulp Fiction", "Quentin Tarantino", 1994)

    print_data_from_table()

    edit_film(1, new_release_year=1994)
    print_data_from_table()
    delete_all_table_data()
