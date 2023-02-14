"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__= "playlists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Playlist %r>' % self.name
    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""
    __tablename__= "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Songs %r>' % self.id
    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    playlist = db.relationship('Playlist', backref=db.backref('playlists', cascade='all, delete-orphan'))
    song = db.relationship('Song', backref=db.backref('songs', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Playlist_songs %r>' % self.id
    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
