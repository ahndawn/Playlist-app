"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, DataRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    playlist_id = IntegerField('Playlist ID', validators=[DataRequired()])
    song_id = IntegerField('Song ID', validators=[DataRequired()])
    submit = SubmitField('Add Song to Playlist')
