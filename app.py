from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

with app.test_request_context():    
    connect_db(app)
    db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)



@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get(playlist_id)
    return render_template('playlist.html', playlist=playlist)
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK - DONE


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    if form.validate_on_submit():
        playlist = Playlist(name=form.name.data, description=form.description.data)
        db.session.add(playlist)
        db.session.commit()
        return redirect(f"/playlists")
    return render_template('new_playlist.html', form=form)
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK - DONE


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def song_details(song_id):
    song = Song.query.get(song_id)
    if not song:
        return "Song not found", 404
    return render_template("song.html", song=song)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK - DONE


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    if form.validate_on_submit():
        # Add the new song to the database
        title = form.title.data
        artist = form.artist.data
        # adding the new song to SQLAlchemy database
        new_song = Song(title=title, artist=artist)
        db.session.add(new_song)
        db.session.commit()
        return redirect(f"/songs")
    return render_template('new_song.html', form=form)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""
    form = NewSongForPlaylistForm()
    if form.validate_on_submit():
        song = Song(title=form.title.data, artist=form.artist.data)
        db.session.add(song)
        db.session.commit()
        playlist_song = Playlist(playlist_id=playlist_id, song_id=song.id)
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(f"/playlists")
    songs = Song.query.all()
    return render_template('add_song_to_playlist.html', form=form, songs=songs)
    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK - DONE

    # # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    # playlist = Playlist.query.get_or_404(playlist_id)
    # form = NewSongForPlaylistForm()

    # # Restrict form to songs not already on this playlist

    # curr_on_playlist = ...
    # form.song.choices = ...

    # if form.validate_on_submit():

    #       # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    #       return redirect(f"/playlists/{playlist_id}")

    # return render_template("add_song_to_playlist.html",
    #                          playlist=playlist,
    #                          form=form)
