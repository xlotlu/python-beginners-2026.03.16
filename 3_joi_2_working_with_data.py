# Dat fiind dataset-ul din 'data/books.csv',
# obțineți un raport cu numărul de cărți / genre.

import csv

def book_count_genre(csvfile):
    """
    loads data from the given csv file
    and returns a dictionary
    with the number of books per genre
    """

    counts = {}

    with open(csvfile) as f:
        reader = csv.DictReader(f)

        for row in reader:
            # row is now a dict
            genre = row["Genre"]

            # we must now increment the existing value
            # under the `counts` dictionary.
            #
            # but, we must first know if there /is/
            # an existing value.

            # v1. we can do it with try / except
            try:
                old_count = counts[genre]
            except KeyError:
                old_count = 0

            # v2. we can do it with if / else
            if genre in counts:
                old_count = counts[genre]
            else:
                old_count = 0
            
            # v3. we use a default
            old_count = counts.get(genre, 0)


            # and now we set the new value
            counts[genre] = old_count + 1

    return counts

book_count_genre('data/books.csv')