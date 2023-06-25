// Remember to change the settings based on your choice!

const ap = new APlayer({
  container: document.getElementById('aplayer'),
  lrcType: 3,
  fixed: true,
  volume: 0.7,
  mutex: true,
  audio: [{
    name: 'name',
    artist: 'artist',
    url: 'audio/example.mp3',
    cover: 'audio/cover.png',
    lrc: 'audio/lrc.lrc'
  }]
});
