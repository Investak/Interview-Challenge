/**
 * common js constants for the project
 */

var Highcharts = require('highcharts/highstock');

/**
 * app global settings
 */
var settings = {
  // this is the loader animation for all interactions
  loader_options: {
    lines: 17, // The number of lines to draw
    length: 12, // The length of each line
    width: 28, // The line thickness
    radius: 55, // The radius of the inner circle
    scale: 0.15, // Scales overall size of the spinner
    corners: 1, // Corner roundness (0..1)
    color: '#000', // #rgb or #rrggbb or array of colors
    opacity: 0, // Opacity of the lines
    rotate: 0, // The rotation offset
    direction: 1, // 1: clockwise, -1: counterclockwise
    speed: 1.5, // Rounds per second
    trail: 54, // Afterglow percentage
    fps: 20, // Frames per second when using setTimeout() as a fallback for CSS
    zIndex: 2e9, // The z-index (defaults to 2000000000)
    className: 'customspinner', // The CSS class to assign to the spinner
    top: '50%', // Top position relative to parent
    left: '50%', // Left position relative to parent
    shadow: false, // Whether to render a shadow
    hwaccel: false, // Whether to use hardware acceleration
    position: 'relative' // Element positioning
  },

  // chart settings
  charts: {
    defaults: function() {
	  	return {
	      rangeSelector: { // time-range selector 
	        selected: 1
	      },
	      yAxis: {
	        labels: {
	          formatter: function () {
	            return (this.value > 0 ? ' + ' : '') + this.value + '%';
	          }
	        },
	        plotLines: [{
	          value: 0,
	          width: 2,
	          color: 'silver'
	        }]
	      },
	      plotOptions: {
	        series: {
	          compare: 'percent'
	        }
	      },
	      tooltip: {
	        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
	        valueDecimals: 2
	      },
	      credits: {
	        enabled: false
	      },
	      series: [] // defined by each chart instance...
	    }
	  }
  },

  // base url for all requests
  url: '/PlaygroundMgmt'
};

/**
 * Ajax setup to allow sending POST to server
 */
$.ajaxSetup({ 
  beforeSend: function(xhr, _settings) {
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      
      return cookieValue;
    }
    if (!(/^http:.*/.test(_settings.url) || /^https:.*/.test(_settings.url))) {
      // Only send the token to relative URLs i.e. locally.
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  } 
});

module.exports = settings;