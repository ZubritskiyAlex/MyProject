import './App.css';
import {BrowserRouter as Router,Route , Switch,} from "react-router-dom";
import {Header} from "./components/Header/Header";
import {Footer} from "./components/Footer/Footer";
import {ProductContent} from "./containers/ProductContent/ProductContent";
import {LoginPage} from "./containers/LoginPage/LoginPage";
import {About} from "./components/About/about";
import {AddProductForm} from "./containers/ProductContent/components/AddProductForm";
import {Component, useState} from "react";
import {connect} from "react-redux";


import './store'
import {setProducts} from "./actions/products";

//const [isLoggedIn, setIsLoggedIn] = useState(localStorage.getItem('isLoggedIn') === 'true');
//const [userName, setUserName] = useState(localStorage.getItem('userName'));



class App extends Component {


    render() {
        const {products} = this.props.products
        const {setProducts} = this.props;
        const newProducts = [
            {
                id:0,
                title: 'asfasdgasdg -' + new Date()
            }
        ];
        return (
            <Router>
                <div className="App">
                    <Header
                       // userName={userName}
                       // isLoggedIn={isLoggedIn}
                       // setIsLoggedIn={setIsLoggedIn}
                    />


                             <h1>{products[0].title}</h1>
                             <button onClick={setProducts.bind(this, newProducts)}>Set new products</button>
                    <main>
                        <Switch>
                            <Route exact path="/products" component={ProductContent}/>
                            <Route exact path="/productcreate" component={AddProductForm}/>

                            <Route exact path="/login" component={LoginPage}
                                  />



                            <Route exact path="/" component={About}/>


                        </Switch>
                    </main>

                    <Footer year={new Date().getFullYear()}/>
                </div>
            </Router>
        );
    }
}

const mapStateToProps = state =>({
   ...state
});

const mapDispatchToProps = dispatch => ({
    setProducts: products => dispatch(setProducts(products))
});



export default connect(mapStateToProps, mapDispatchToProps)(App);
