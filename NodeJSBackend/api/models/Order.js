// app/models/Order.js

var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var OrderSchema   = new Schema({
	id :int,
    name: String,
	milk:String,
	size:String
});

module.exports = mongoose.model('Order', OrderSchema);