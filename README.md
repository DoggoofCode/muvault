# Muvault
Muvault is _still in development_ please contribute when you see the time!

## Goal

The goal for Muvault is to be similar to git, where you can push and pull from remote servers, add music and share music as such. 

### Main Specifications

Music will be broken down into album chunks, folders which contain the music. Within each album, there should be an info.toml containing data pertanante to the album, which is:
* List of all songs and their file names in the directory
* The author(s) of the track 
* The genre of the track

_(and more)_

1. `muvault remote`

The remote sub function should be used to add or edit a remote server used to access offloaded music. 

2. `muvault ls`

This function should request a full manifest of all music stored on the local storage device, then allow the user to search through the catalog.  

3. `muvault push <album-name>`

Generates an info.toml file and tags all music before pushing it onto the local registry. 

4. `muvault pull <album-name>`

Using an album identified from `muvault ls`, it pulls an album straight into your music directory!

5. `muvault storage`

Changes the method of storage, by just placing all the albums into a folder, organizing by genre, etc.

