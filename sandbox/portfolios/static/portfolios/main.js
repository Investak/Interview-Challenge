var Box = React.createClass({
  getInitialState() { return {items:[]} },
  componentDidMount() { this.setState({items: this.props.items}) },
  handleSubmit(item) {
    // After Ajax call success
    item.id = Date.now();
    this.setState({items: items.concat([item])});
  },
  render() {
    return (
      <div className="mdl-grid">
        <div className="itemBox mdl-cell mdl-cell--4-col">
          <ItemForm onSubmit={this.handleSubmit}/>
          <ItemList items={this.state.items}/>
        </div>
        <div className="itemBox mdl-cell mdl-cell--8-col">
          <Chart />
        </div>
      </div>
    )
  }
});

var Chart = React.createClass({
  render() {
    return (<h1></h1>);
  }
})

// Stores no state, simply displays passed properties
const ItemList = React.createClass({
  onItemClick(id) {

  },
  render() {
    let list_items = this.props.items.map(item => <Item text={item.text} key={item.text} display={item.display} onClick={() => onItemClick(item.text)}>{item.text}</Item>);
    return (
      <ul>{list_items}</ul>
    );
  }
});

var ItemForm = React.createClass({
  getInitialState() { return {text:'', display:true} },
  handleTextChange(e) { this.setState({text: e.target.value}) },
  handleDisplayChange(e) { this.setState({display: Boolean(e.target.value}) },
  handleSubmit(e) {
    e.preventDefault();
    var text = this.state.text.trim();
    if(text) {
      this.props.onSubmit({text});
      this.setState({text:''});
    }
  },
  render() {
    return (
      <form className="commentForm" onSubmit={this.handleSubmit}>
        <input type="text" placeholder="YHOO" list="symbols" value={this.state.text} onChange={this.handleTextChange}/>
        <input type="submit" value="Choose" />
      </form>
    );
  }
});

const Item = React.createClass({
  render() {
    return (
      <li 
        onClick={this.props.onClick} 
        style={{textDecoration: this.props.display ? 'line-through' : 'none'}}>
        {this.props.text}
      </li>
    )
  }
});

var Link = React.createClass({
  render() {
    if(this.props.active) {
      return <span>{this.props.children}</span>
    }

    return (
      <a href="#" onClick={e => {e.preventDefault(); this.props.onClick()}}>{this.props.children}</a>
    )
  }
})
const list = [{symbol:"YHOO"}];
ReactDOM.render(<Box items={list}/>, document.getElementById('mountNode'));


const ADD_ITEM = 'ADD_ITEM'
const REMOVE_ITEM = 'REMOVE_ITEM'

function addItem(text) {
  return {
    type: ADD_ITEM,
    text
  }
}

function removeItem(id) {
  return {
    type: REMOVE_ITEM,
    id
  }
}

const boundAddItem = text => dispatch(addItem(text))

const initialState = { items: [] }

function items(state = [], action) {
  var newState;
  switch(action.type) {
    case ADD_ITEM:
      newState = [...state, action.text]
      break;
    case REMOVE_ITEM:
    default:
      newState = state
  }
  return newState;
}

const getItems = (items, filter) => {
  switch(filter) {
    case 'SHOW_ALL':
      return items;
    case 'SHOW_ACTIVE':
      return items.filter(i => i.active)
  }
}
const mapStateToProps = (state) => {
  return {
    items: getItems(state.items, state.visibilityFilter)
  }
}
const itemApp = Redux.combineReducers({items});
let store = Redux.createStore(itemApp)
let unsubscribe = store.subscribe(() => console.log(store.getState()))
store.dispatch(addItem("Learn about actions"));
store.dispatch(addItem("Learn about reducers"));
store.dispatch(addItem("Learn about store"));
unsubscribe();