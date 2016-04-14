var path = require('path');
var webpack = require('webpack');
var express = require('express');
var config = require('./webpack.config');
var proxy = require('proxy-middleware');
var url = require('url');

var app = express();
var compiler = webpack(config);

app.use(require('webpack-dev-middleware')(compiler, {
  noInfo: true,
  publicPath: config.output.publicPath,
  historyApiFallback: true
}));

// proxy to flask server
app.use('/api', proxy(url.parse('http://localhost:5000/api')));

// webpack with reload
app.use(require('webpack-hot-middleware')(compiler));
app.get('*', function(req, res) {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(3000, 'localhost', function (err, result) {
  if (err) {
    console.log(err);
  }

  console.log('Listening at localhost:3000');
});
