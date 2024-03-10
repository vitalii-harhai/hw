from webargs import fields
from webargs.flaskparser import use_kwargs

from tools.db_connection import db_query
from tools.convert import db_response_one_result_to_html


@use_kwargs({
    'track-id': fields.Int(required=True)
},
    location='query')
def get_all_info_about_track(**kwargs: dict) -> str:
    """
    Get all info about track
    :param kwargs: track-id = track ID
    :return: html string with list of all info about track
    """
    track_id = kwargs['track-id']

    query = ('SELECT "Track ID - " || tracks.TrackId, '
             '"Track\'s name - " || tracks.Name, '
             '"Artist\'s name - " || artists.Name, '
             '"Album\'s name - " || albums.Title, '
             '"Genre - " || genres.Name, '
             '"Composer - " || tracks.Composer, '
             '"Media types - " || media_types.Name, '
             '"Playlists - " || (SELECT GROUP_CONCAT(playlists.Name) '
             'FROM playlist_track '
             'JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId '
             'WHERE playlist_track.TrackId = tracks.TrackId) '
             'FROM tracks '
             'LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId '
             'LEFT JOIN genres ON tracks.GenreId = genres.GenreId '
             'LEFT JOIN artists ON albums.ArtistId = artists.ArtistId '
             'LEFT JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId '
             f'WHERE tracks.TrackId = {track_id};')

    results = db_query(query)
    results = db_response_one_result_to_html(results)

    return results
