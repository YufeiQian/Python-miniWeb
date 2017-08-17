import media
import fresh_tomatoes

titles = ['Ghost in the shell', 'Doraemon stand by me', 'My neighbor Totoro']
posters_url = ['https://i.pinimg.com/564x/6b/21/e0/6b21e0541d227aeda425618d4bc73e28.jpg',
               'https://s-media-cache-ak0.pinimg.com/564x/03/8c/53/038c5381e42f5dce3cdc5b00742b443e.jpg',
               'https://s-media-cache-ak0.pinimg.com/564x/20/13/71/2013711acbe7b7774d650232bfab1fb7.jpg']

story_lines = ['A cyber-punk style movie',
               'An anime for children',
               'Miyazaki\'s master piece']

youtube_links = ['https://www.youtube.com/watch?v=p2MEaROKjaE',
                 'https://www.youtube.com/watch?v=RP-KqRkDWS0',
                 'https://www.youtube.com/watch?v=92a7Hj0ijLs']

movie_list = []

for i in range(len(titles)):
    movie = media.Movie(titles[i], story_lines[i], posters_url[i], youtube_links[i])
    movie_list.append(movie)

fresh_tomatoes.open_movies_page(movie_list)