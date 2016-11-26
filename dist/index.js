'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _express = require('express');

var _express2 = _interopRequireDefault(_express);

var _bodyParser = require('body-parser');

var _bodyParser2 = _interopRequireDefault(_bodyParser);

var _http = require('http');

var _http2 = _interopRequireDefault(_http);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var app = (0, _express2.default)();
app.use(_bodyParser2.default.json());

// Routes
app.get('/hello', function (req, res, next) {
    res.status(200).json({ message: 'Hello, World!' });
});

// Error Handlers
app.use(function (req, res, next) {
    var err = new Error();
    err.message = 'Not Found';
    err.status = 404;
    next(err);
});

app.use(function (err, req, res, next) {
    res.status(err.status || 500).json({
        message: err.message,
        error: { err: err }
    });
});

// Boot up HTTP server
app.server = _http2.default.createServer(app);
app.server.listen(3000);

exports.default = app;
//# sourceMappingURL=index.js.map