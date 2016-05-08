/**
 * Global event system
 * for communication between components
 */
var EventEmitter = require('event-emitter'),
	events = new EventEmitter(); // shared instance between all components 

module.exports = events;