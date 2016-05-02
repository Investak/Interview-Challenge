/**
 * Frontend main application controller 
 */
var React = require('react'),
  ReactDOM = require('react-dom'),
  events = require('./Events.js'),
  PfolioList = require('./Pfolio.js').PfolioList,
  Dboard = require('./Dboard'),
  Instruments = require('./Instruments.js');

// Initialize all components
var pfolioList = ReactDOM.render(<PfolioList />, $('#portfolio_list').get(0));
var dboard = ReactDOM.render(<Dboard />, $('#dashboard').get(0));
var instruments = ReactDOM.render(<Instruments />, $('#instrument_box').get(0));

// events grouped by object
// Events coming from Pfolio.js
events.on('PfolioList.LOADED', instruments.pfoliosLoaded);
events.on('PfolioList.UPDATED_PFOLIO_CONTENT', dboard.insAddedToPfolio);
events.on('PfolioItem.OPEN', dboard.openedPortfolio);
events.on('PfolioAdder.NEW_PFOLIO', pfolioList.onNewPfolio);
events.on('PfolioAdder.NEW_PFOLIO', instruments.onNewPfolio);

// Events coming from Dboard.js
events.on('CtrlFolio.DELETED_PFOLIO', pfolioList.onPfolioDeleted);
events.on('CtrlFolio.DELETED_PFOLIO', dboard.onPfolioDeleted);
events.on('CtrlFolio.RENAMED_PFOLIO', pfolioList.onPfolioRenamed);
events.on('CtrlFolio.RENAMED_PFOLIO', dboard.onPfolioRenamed);
events.on('Dboard.REMOVED_FROM_PFOLIO', pfolioList.afterInsRemovedFromPfolio);
events.on('InsBtn.TOGGLE_CHART_SERIES', dboard.toggleSeries);
events.on('InsBtn.REMOVE', dboard.removeInsFromPfolio);

// Events coming from Instruments.js
events.on('InstrumentResult.CLICK', instruments.onInsSelected);
events.on("Instruments.ADDED_TO_PFOLIO", pfolioList.afterInsAddedToPfolio);