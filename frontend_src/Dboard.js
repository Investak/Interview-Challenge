/**
 * Controller for app Dashboard
 * here the instruments of a particular portfolio are loaded
 * and the different charts can be opened
 */
var React = require('react'),
  ReactDOM = require('react-dom'),
  SETTINGS = require('./settings.js'),
  main = require('./Main.js'),
  events = require('./Events.js'),
  PerfChart = require('./Charting.js').PerfChart,
  BusyMsgs = require('./BusyMsgs.js'),
  Modal = require('react-modal');

/**
 * window to display the Inss/instruments the select portfolio has
 * and to display the performance chart. 
 */
var Dboard = React.createClass({
  getInitialState: function () {
    return {
      currentPfolio: null,
      cAction: {
        type: 'none'
      }
    }
  },

  openedPortfolio: function (pfolio) {
    if (this.state.currentPFolio == pfolio) // the same, no action
      return;

    this.setState({
      currentPfolio: pfolio,
      cAction: {
        type: 'switchChart'
      }
    }); // update and render...
  },

  insAddedToPfolio: function (npfolios) {
    npfolios.portfolios.forEach(function (elm) {
      if(elm.id === this.state.currentPfolio.id)
        this.setState({
          currentPfolio: elm,
          cAction: {
            type: 'switchChart'
          }
        });
    }.bind(this));
  },

  removeInsFromPfolio: function (instrument) {
    $.ajax({
      url: SETTINGS.url + '/portfolio_del_ins',
      method: 'POST',
      dataType: 'json',
      data: {portfolio_id: this.state.currentPfolio.id, instrument_id: instrument.id},
      cache: false,
      success: function(_data) {
        // TODO... server status

        // fade out the instrument
        $("#InsBtn_" + instrument.id).fadeOut();

        // Pfolio internal data will change
        events.emit("Dboard.REMOVED_FROM_PFOLIO", _data);
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(err.toString());
      }.bind(this)
    });
  },

  onPfolioDeleted: function () {
    this.setState({currentPfolio: null})
  },

  onPfolioRenamed: function (ndata) {
    this.insAddedToPfolio(ndata); // for now, they have the same effect
  },

  toggleSeries: function (insBtnData) {
    this.setState({
      cAction: { 
        type: 'toggleSeries',
        insBtnData: insBtnData
      }
    });
  },

  render: function () {
    if (this.state.currentPfolio === null) // nothing selected
      return (<div>Please select one of the portfolio from the left panel to view its details</div>);
    else
      return (
        <div className="row dashboard col-lg-12">
          <div>
            <div style={{float: "left"}} >
              <h3>Current Portfolio: </h3>
            </div>
            <CtrlFolio pfolio={this.state.currentPfolio} />
            <div style={{clear: "both"}} />
          </div>
          <InsList instruments={this.state.currentPfolio.instruments} />

          <PerfChart cAction={this.state.cAction} instruments={this.state.currentPfolio.instruments} />
        </div>
      );
  }
});

/**
 * list of Instruments buttons belonging to a portfolio
 */
var InsList = React.createClass({
  getInsBtns: function () {
    var btns = this.props.instruments.map(function (instrument) {
      return (
        <InsBtn key={instrument.id} name={instrument.name} instrument={instrument} />
      );
    });

    return btns;
  },

  render: function () {
    if(!this.props.instruments.length)
      return (
        <div>You haven't added any instruments yet. Please see the "Instruments" panel in the left to explore a wide variety of stocks, commodities, etc. and include them in your portfolios. 
        </div>
      );
    else
      return (
        <ul id="instruments_list">
          {this.getInsBtns()}
          <div style={{clear:"both"}}></div>
        </ul>
      );
  }
});

/**
 * Instrument button to display in dashboard,
 * enables two possible actions:
 *  - activate/deactivate performance line for this instrument
 *  in general perormance chart
 *  - detail button that will load new history chart specific
 *  to that instrument
 */
var InsBtn = React.createClass({
  getInitialState: function () {
    return {displayClass: "stock-btn"};
  },

  chartAction: function () {
    var switching = 'on';
    if (this.state.displayClass.indexOf('stock-disabled') >= 0) {
      this.setState({displayClass: "stock-btn"});
    }
    else {
      this.setState({displayClass: "stock-btn stock-disabled"});
      switching = 'off';
    }
    
    events.emit('InsBtn.TOGGLE_CHART_SERIES', {
      switching: switching, 
      instrument: this.props.instrument
    });
  },

  removeIns: function () {
    events.emit('InsBtn.REMOVE', this.props.instrument);
    event.stopPropagation();
  },

  insChart: function (event) {
    // TODO...
    alert('this function will display the indivdual candlechart of the instrument. Not yet available...');
    event.stopPropagation();
  },

  render: function () {
    return (
      <div onClick={this.chartAction} className={this.state.displayClass} id={"InsBtn_" + this.props.instrument.id}>
        {this.props.name}
        <button onClick={this.insChart} className="btn btn-primary btn-xs" title="View history chart of this instrument">
          <span className="glyphicon glyphicon-equalizer"></span>
        </button>
        <button onClick={this.removeIns} className="btn btn-danger btn-xs" title="Remove this instrument from the portfolio">
          <span className="glyphicon glyphicon-trash"></span>
        </button>
      </div>
    );
  }
});

/**
 * Provide edit and delete functions inside the 
 * dashboard panel
 */
var CtrlFolio = React.createClass({
  getInitialState: function () {
    return ({
      typing: false,
      confirmingDel: false,
      serverStatus: {
        type: 'none',
        text: ''
      }
    });
  },

  editName: function () {
    $('.portfolio-edit-input').val(this.props.pfolio.name);
    this.setState({typing: true});
  },

  updatePfolioName: function () {
    // busymsg
    this.setState({
      serverStatus: {
        type: 'updating',
        text: 'updating'
      }
    });

    $.ajax({
      url: SETTINGS.url + '/portfolio_edit',
      method: 'POST',
      dataType: 'json',
      data: {portfolio_id: this.props.pfolio.id, portfolio_name: $('.portfolio-edit-input').val()},
      cache: false,
      success: function(_data) {
        this.setState({
          serverStatus: {
            type: 'success',
            text: 'name changed' 
          }
        });

        // pfolioList will change the name listed
        events.emit('CtrlFolio.RENAMED_PFOLIO', _data);
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(err.toString());
      }.bind(this)
    });
  },

  lostFocus: function () {
    this.setState({typing: false});
  },

  delConfirm: function () {
    this.setState({confirmingDel: true});
  },

  afterDelConfirm: function () {
    // busymsg
    $('.modal.in').modal('hide');
    this.setState({
      serverStatus: {
        type: 'updating',
        text: 'deleting this portfolio'
      }
    });

    $.ajax({
      url: SETTINGS.url + '/portfolio_delete',
      method: 'POST',
      dataType: 'json',
      data: {portfolio_id: this.props.pfolio.id},
      cache: false,
      success: function(_data) {
        this.setState({
          serverStatus: {
            type: 'success',
            text: 'Portfolio deleted!' 
          }
        });

        // dboard will close this deleted pfolio
        // and Pfolio list will remove it too
        events.emit('CtrlFolio.DELETED_PFOLIO', _data);
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(err.toString());
      }.bind(this)
    });
  },

  afterSuccess: function () {
    this.setState({
      typing: false,
      serverStatus: {
        type: 'none',
        text: ''
      }
    });
  },

  render: function () {
    if(this.state.serverStatus.type !== 'none') // displaying busy msg
      return (
        <BusyMsgs id={"ctrl-pfolio-busymsg"} status={this.state.serverStatus} succCallback={this.afterSuccess} />
      );
    else if (this.state.typing) // editing the pfolio name
      return (
        <div className={"input-group"}>
          <input type={"text"} className="portfolio-edit-input" placeholder={"Portfolio name"} defaultValue={this.props.pfolio.name} />
          <div className="portfolio-add-ctrls">
            <div onClick={this.lostFocus} className="btn btn-default portfolio-add-send">Cancel</div>
            <div onClick={this.updatePfolioName} className="btn btn-default portfolio-add-cancel">Ok</div>
            <div style={{clear: "both"}} />
          </div>
        </div>
      );
    else
      return (
        <div>
          <div className="modal fade bs-example-modal-sm" tabindex={"-1"} role={"dialog"} aria-labelledby={"mySmallModalLabel"}>
            <div id={"modalDelPfolio"} className="modal-dialog modal-sm">
              <div className="modal-content">
                <div className={"portfolio-del-dialog"}><b>Are you sure you want to delete the portfolio?</b><br /> 
                This action can't be reversed</div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-default" data-dismiss="modal">Cancel</button>
                  <button type="button" className="btn btn-primary" onClick={this.afterDelConfirm}>Delete</button>
                </div>
              </div>
            </div>
          </div>
          <h3 className="dboard-pfolio-title">{this.props.pfolio.name}</h3>
          <div className="btn btn-default dboard-pfolio-btn" onClick={this.editName}>
            <span className="glyphicon glyphicon-pencil"></span>
          </div>
          <div className="btn btn-default dboard-pfolio-btn" data-toggle="modal" data-target=".bs-example-modal-sm" onClick={this.delConfirm}>
            <span className="glyphicon glyphicon-trash"></span>
          </div>
        </div>
      );
  }
});

module.exports = Dboard;