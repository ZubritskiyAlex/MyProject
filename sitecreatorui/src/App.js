import './App.css';
import {Component} from "react";
import Sidebar from "./containers/Sidebar";
import {BrowserRouter as Router, Switch,  Route} from "react-router-dom";
import ProductListing from "./containers/ProductListing";
import ProductDetail from "./containers/ProductDetail";
import ShopListing from "./containers/ShopListing";
import ShopDetail from "./containers/ShopDetail";


class App extends Component{

    render() {
        return(
            <div className="App">
                <Router>
                    <Sidebar/>
                    <Switch>
                        <Route path="/" exact component={ShopListing}/>
                        <Route path="/shop/:shopId" exact component={ShopDetail}/>
                        <Route path ='/products' exact component={ProductListing} />
                        <Route path="/product/:productId" exact component={ProductDetail}/>
                        <Route> 404 Not Found!</Route>
                    </Switch>
                </Router>
            </div>
        );
    }
}

export default App;