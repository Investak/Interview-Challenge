/**
 * Full management of charts displayed
 * in the dashboard
 * currently with HighCharts: http://www.highcharts.com/
 */
var React = require('react'),
  ReactDOM = require('react-dom'),
  Highcharts = require('highcharts/highstock'),
  SETTINGS = require('./Settings.js'),
  events = require('./Events.js');

/**
 * Highchart handler
 * this is for the performance charts
 */
var PerfChart = React.createClass({
  getInitialState: function () {
    return {chartActive: false};
  },

  componentDidMount: function () {
    this.initCharting(this.props);
  },

  componentWillReceiveProps: function (nprops) {
    if(nprops.cAction.type === 'toggleSeries')
      this.toggleSeries(nprops.cAction.insBtnData);
    else if (nprops.cAction.type === 'switchChart')
      this.switchChart(nprops.instruments);
  },

  toggleSeries: function (insBtnData) {
    var series = $('#test_chart').highcharts().get('s_' + insBtnData.instrument.id);
    switch (insBtnData.switching) {
      case 'off':
        series.hide();
        break;
      case 'on':
        series.show();
    }
  },

  initCharting: function (props) {
    // load performance series for the instruments
    props.instruments.forEach(function (instrument) {
      $.ajax({
        url: SETTINGS.url + '/portfolio_performance',
        method: 'GET',
        data: {ticker: instrument.ticker},
        dataType: 'json',
        cache: false,
        success: function(_data) {
          this.setChart(_data, instrument);
        }.bind(this),
        error: function(xhr, status, err) {
          console.error(err.toString());
        }.bind(this)
      });
    }.bind(this));
  },

  setChart(_data, instrument) {
    // data adjustments for charting
    _data = JSON.parse(_data);
    _data.history.reverse();
    _data = _data.history.map(function (h) {
      return [(new Date(h.Date)).getTime(), (parseFloat(h.High) + parseFloat(h.Low)) / 2];
    });

    var nseries = {'name': instrument.name, data: _data, id: 's_' + instrument.id};
    if (this.state.chartActive === false) {
      var opts = SETTINGS.charts.defaults(); // load standard options
      opts.series.push(nseries);
      $("#test_chart").highcharts("StockChart", opts);
      
      this.setState({chartActive: true});
    }
    else
      $("#test_chart").highcharts().addSeries(nseries);
  },

  switchChart: function (nprops) {
    if(this.state.chartActive) {
      $("#test_chart").highcharts().destroy();
      this.setState({chartActive: false});
    }

    if(nprops.instruments.length)
      this.initCharting(nprops);
  },

  render: function() {
    return (
      <div className="perfchart">
        <div id="test_chart"></div>
      </div>
    );
  }
});

/**
 * Candle Chart
 * this is for individual stocks/instruments window
 * display instrument history as a standard candlestick series
 */
var CandleChart = React.createClass({
  render: function () {
    if (this.props.instrument === null)
      return (<div></div>);
    else
      return (
        <div className="candlechart-cont">&lt;candlestick chart will load here&gt;</div>
      );
  }
});

module.exports = {
  PerfChart: PerfChart,
  CandleChart: CandleChart
};