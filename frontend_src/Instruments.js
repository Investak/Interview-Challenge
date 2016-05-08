/**
 * Instrument box to view other stocks, indexes, etc
 * and add them to portfolios
 */
var React = require('react'),
  ReactDOM = require('react-dom'),
  events = require('./Events.js'),
  SETTINGS = require('./settings.js'),
  CandleChart = require('./Charting.js').CandleChart,
  Loader = require('react-loader'),
  BusyMsgs = require('./BusyMsgs.js');

// this component can't be loaded with the usual require
import SearchInput, {createFilter} from 'react-search-input'

var InstrumentsWindow = React.createClass({
  render: function () {
    return (
      <div className="container">
        <div className="row"> 
          <div className="col-lg-8 w-close-bar">
            <div className="w-title">Search for Instruments</div>
            <a href="#" className="w-close-btn" onClick={this.props.onClose}>
              <span className="glyphicon glyphicon-remove"></span> Close
            </a>
          </div>  
        </div>
        <div className="row"> 
          <div className="col-lg-8 w-result-chart">
            {this.props.children}
          </div>
        </div>
      </div>
    );
  }
});

/**
 * Instruments box controls:
 * - search for instruments
 * - load chart of a specific instrument
 * - add a selected instrument to one of the portfolios
 */
var Instruments = React.createClass({
  getInitialState: function () {
    return {
      visible: false, 
      currentIns: null,
      pfolios: null,
      serverStatus: {
        type: 'none',
        text: ''
      }
    };
  },

  componentWillMount: function () {
    // jquery click to index.html instruments link
    $("#instruments_link").on('click', function() {
      this.setState({visible: true});
    }.bind(this));
  },

  onInsSelected: function (instrument) {
    this.setState({currentIns: instrument});
  },

  pfoliosLoaded: function (pfolios) {
    this.setState({pfolios: pfolios});
  },

  onNewPfolio: function (newf) {
    var pfolios = this.state.pfolios;
    pfolios.push(newf);
    this.setState({pfolios: pfolios});
  },

  getAvailablePfolios: function () {
    var pfolios = this.state.pfolios.map(function (pfolio) {
      return (
        <li className="instruments-pfolio-item" id={pfolio.id}
          key={pfolio.id} onClick={this.addInsToPfolio}
        >
          {pfolio.name}
        </li>);
    }.bind(this));

    return (
      <ul className="dropdown-menu" aria-labelledby="dLabel">
        {pfolios}
      </ul>
    );
  },

  addInsToPfolio: function (event) {
    // busymsg
    this.setState({
      serverStatus: {
        type: 'updating',
        text: 'Adding instrument to portfolio' // TODO: improve this with the name of the entities
      }
    });

    event.persist();
    // send to server 
    $.ajax({
      url: SETTINGS.url + '/portfolio_add_ins',
      method: 'POST',
      dataType: 'json',
      data: {portfolio_id: event.target.id, instrument_id: this.state.currentIns.id},
      cache: false,
      success: function(_data) {
        this.setState({
          serverStatus: {
            type: 'success',
            text: 'successfully added to portfolio' // TODO: improve this with the name of the entities
          }
        });

        // Dboard needs to update based on this
        events.emit("Instruments.ADDED_TO_PFOLIO", {ndata: _data, pfolio_id: event.target.id});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(err.toString());
      }.bind(this)
    });
  },

  closeWindow: function () {
    this.setState({visible: false});
  },

  render: function () {
    if(!this.state.visible)
      return (<div></div>);
    else {
      var ctrl = function () {
        if (this.state.currentIns !== null)
          return (
            <div className="ins-ctrl">
              <h4>{this.state.currentIns === null ? '' : this.state.currentIns.name}</h4>
              <h4>Add to portfolio:</h4>
              <div className="dropdown instruments-add">
                <button id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Select Portfolio<span className="caret"></span>
                </button>
                {this.getAvailablePfolios()}
              </div>
              <CandleChart className="instruments-candlechart" instrument={this.state.currentIns} />
            </div>
          );
        else
          return null;
      }.bind(this);

      return (
        <InstrumentsWindow onClose={this.closeWindow}>
          <div>
            <BusyMsgs id={"instruments-busymsg"} status={this.state.serverStatus} />
            <SearchHandler />
            {ctrl()}
            <div style={{clear: "both"}} />
          </div>
        </InstrumentsWindow>
      );
    }
  }
});

/**
 * Control search for instruments and search results
 */
var SearchHandler = React.createClass({
  getInitialState: function () {
    return {
      searchTerm: '', 
      instruments: [],
      instrumentsLoaded: false
    };
  },

  shouldComponentUpdate: function(nextProps, nextState) {
    // the search handler doesn't re-render after loading everything
    if(this.state.instrumentsLoaded === true && this.state.searchTerm === nextState.searchTerm)
      return false;

    return true;
  },

  componentWillMount: function () {
    // load the instruments from server
    // 
    // TODO:
    // do this with async pagination to have quick response for the user
    $.ajax({
      url: SETTINGS.url + '/instruments_list',
      method: 'GET',
      dataType: 'json',
      cache: true,
      success: function(_data) {
        this.setState({instruments: _data.instruments, instrumentsLoaded: true});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(err.toString());
      }.bind(this)
    });
  },

  onSearch: function (term) {
    this.setState({searchTerm: term});
  },

  getResults: function (filteredIns) {
    return filteredIns.map(function (ins) {
      return (<InstrumentResult instrument={ins} key={ins.id} />);
    }.bind(this));  
  },

  render: function () {
    var instruments = this.state.instruments;
    var filtered = instruments.filter(createFilter( /* createFilter imported */
      this.state.searchTerm, 
      ['name']
    ));

    return (
      <div className="search-handler">
        <SearchInput className="search-input" onChange={this.onSearch} />
        <Loader loaded={this.state.instrumentsLoaded} options={SETTINGS.loader_options}>
          <div className="search-results-block">
            {this.getResults(filtered)}
          </div>
        </Loader>
      </div>
    );
  }  
});

/**
 * search results items
 */
var InstrumentResult = React.createClass({
  /**
   * emits:
   * InstrumentResult.CLICK
   */
  selectCallback: function () {
    events.emit('InstrumentResult.CLICK', this.props.instrument);
  },

  render: function () {
    return (
      <div className="ins-search-item" key={this.props.instrument.id} 
        onClick={this.selectCallback} 
      >
        {this.props.instrument.name}
      </div>
    );
  }
});

module.exports = Instruments;