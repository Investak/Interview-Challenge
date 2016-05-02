/**
 * general loading message for informing
 * the user specific server actions
 */
var React = require('react'),
  ReactDOM = require('react-dom');

/**
 * status to inform the user of a process
 * in action can be of the form:
 *     status: {
 *       type: 'updating',
 *       text: 'doing something with the server'
 *     }}
 *
 *  for success msg:
 *  	status: {
 *  		serverStatus: {
 *        type: 'success',
 *        text: 'Portfolio deleted!' 
 *      }
 *  	}
 * 
 * or for no message:
 *     status: {
 *       type: 'none',
 *       text: ''
 *     }
 *
 * TODO:
 *    ADD error msgs
 */
var BusyMsgs = React.createClass({
  _anim: null,
  _p: ' ...',

  componentWillUpdate: function (nextProps, nextState) {
    if (this.props.status.type === 'updating' && this.props.status.type !== nextProps.status.type)
    	if (this._anim !== null) {
        clearInterval(this._anim);
        this._anim = null;
      }
		if (this.props.status.type === 'success' && this.props.status.type !== nextProps.status.type)
    	$('#' + this.props.id).show();
  },

  innerLoadingAnim: function () {
    this._anim = setInterval(function() {
      if (this._p.length > 18)
        this._p = ' ...';
      document.getElementById('BusyMsg_inner_txt').innerHTML = this._p;
      this._p += '.';
    }.bind(this), 50);
  },

  innerSuccAnim: function () {
    $('#' + this.props.id).fadeOut(function () {
    	this.props.succCallback();
    }.bind(this));
  },

  render: function () {
    switch(this.props.status.type) {
      case 'updating':
        this.innerLoadingAnim();
        return (
          <div id={this.props.id} className="alert alert-info" role="alert">
            {this.props.status.text}
            <span id="BusyMsg_inner_txt"></span>
          </div>
        );
      
        case 'success':
          setTimeout(this.innerSuccAnim, 1000);
          return (
            <div id={this.props.id} className="alert alert-success" role="alert">
              {this.props.status.text}
            </div>
          );

      case 'none':
      default:
        return null;
    }
  }
});

module.exports = BusyMsgs;
