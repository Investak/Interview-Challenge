/**
 * Controller for portfolios
 */
var React = require('react'),
  ReactDOM = require('react-dom'),
  events = require('./Events.js'),
  SETTINGS = require('./Settings.js'),
  BusyMsgs = require('./BusyMsgs.js');

/**
 * Full list of portfolio items encapsulating
 * portfolio-crud related operations and sending events to
 * other components in main.
 */
var PfolioList = React.createClass({
  getInitialState: function() {
    return {
      data: {
        portfolios: []
      }
    };
  },

  componentDidMount: function () {
    this.loadPortfolios();
  },

  loadPortfolios: function () {
    $.ajax({
      url: SETTINGS.url + '/portfolio_list',
      method: 'GET',
      dataType: 'json',
      cache: false,
      success: function(_data) {
        this.setState({data: _data});

        // Instruments component listens to this
        events.emit("PfolioList.LOADED", this.state.data.portfolios);
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(err.toString());
      }.bind(this)
    });
  },

  getPortfolioElms: function () {
    var pfolios = this.state.data.portfolios.map(function (item) {
      return (
        <PfolioItem name={item.name} key={item.id} id={item.id} pfolio={item} />
      );
    });

    return pfolios;
  },

  afterInsAddedToPfolio: function (results) {
    this.setState({data: results.ndata});
    
    events.emit("PfolioList.UPDATED_PFOLIO_CONTENT", this.state.data);
  },

  afterInsRemovedFromPfolio: function (ndata) {
    this.setState({data: ndata});
  },

  onNewPfolio: function (npfolio) {
    var data = this.state.data;
    data.portfolios.push(npfolio);

    this.setState({data: data});
  },

  onPfolioDeleted: function (ndata) {
    this.setState({data: ndata});
  },

  onPfolioRenamed: function (ndata) {
    this.onPfolioDeleted(ndata); // for now, they have the same efect for this component
  },

  render: function () {
    return (
      <div>
        <ul className="portfolio_ul">{this.getPortfolioElms()}</ul>
        <PfolioAdder />
      </div>
    );
  }
});

/**
 * Specific Portfolio Item functionality
 */
var PfolioItem = React.createClass({
  openPortfolio: function (evt) {
    events.emit('PfolioItem.OPEN', this.props.pfolio); // Dboard will handle this
  },

  render: function () {
    return (
      <li>
        <a id={this.props.id} className="portfolio_a" onClick={this.openPortfolio}>{this.props.name}</a>
      </li>
    );
  }
});

/**
 * Portfolio adder
 * handles new portfolio creation
 */
var PfolioAdder = React.createClass({
  getInitialState: function () {
    return {
      typing: false,
      serverStatus: {
        type: 'none',
        text: ''
      }
    }
  },

  startTyping: function () {
    this.setState({typing: true});
  },

  lostFocus: function () {
    this.setState({typing: false});
    $('.portfolio-add-input').val('');
  },

  sendPfolio: function (event) {
    // server busy status
    this.setState({
      typing: false,
      serverStatus: {
        type: 'updating',
        text: 'Saving'
      }
    });

    // send porftolio to server
    $.ajax({
      url: SETTINGS.url + '/portfolio_create',
      method: 'POST',
      dataType: 'json',
      data: {name: $('.portfolio-add-input').val()},
      cache: false,
      success: function(_data) {
        this.setState({
          serverStatus: {
            type: 'success',
            text: 'Portfolio created!' // TODO: improve this with the name of the entities
          }
        });

        // list of portfolios in Instruments dropdown will update
        events.emit("PfolioAdder.NEW_PFOLIO", _data);
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(err.toString());
      }.bind(this)
    });
  },

  afterSuccess: function () {
    this.setState({
      serverStatus: {
        type: 'none',
        text: ''
      }
    });
  },

  render: function () {
    if (this.state.typing)
      return (
        <div className="input-group">
          <input type={"text"} className="portfolio-add-input" placeholder={"Portfolio name"} />  
          <div className="portfolio-add-ctrls">
            <div onClick={this.lostFocus} className="btn btn-default portfolio-add-send">Cancel</div>
            <div onClick={this.sendPfolio} className="btn btn-default portfolio-add-cancel">Ok</div>
            <div style={{clear: "both"}} />
          </div>
        </div>
      );
    else if (this.state.serverStatus.type !== 'none') {
      return (
        <BusyMsgs id={"portfolio-add-busymsg"} status={this.state.serverStatus} succCallback={this.afterSuccess} />
      );
    }
    else
      return (
        <div className="btn btn-default" id={"portfolio-add-btn"} onClick={this.startTyping} >
          Add new Portfolio
          <span className="glyphicon glyphicon-plus portfolio-add-sign"></span>
        </div>
      );
  }
});

module.exports = {
  PfolioList: PfolioList,
  PfolioItem: PfolioItem
};