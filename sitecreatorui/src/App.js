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
import axios from "axios";
import Menu from "./components/Menu/Menu";
import {Container} from "semantic-ui-react";
import ProductCard from "./components/Product/ProductCard";


import './store'
import {setProducts} from "./actions/products";

//const [isLoggedIn, setIsLoggedIn] = useState(localStorage.getItem('isLoggedIn') === 'true');
//const [userName, setUserName] = useState(localStorage.getItem('userName'));

import {products} from "./shared/projectData";



class App extends Component {

    componentWillMount() {
        const {setProducts} = this.props
        axios.get('/projectData').then(({data}) => {
            setProducts(data);
        });
    }

    render() {
        const {products, isReady} = this.props;
        return (

            <Router>
                <Container>
                    <Menu/>

                    <Header
                       // userName={userName}
                       // isLoggedIn={isLoggedIn}
                       // setIsLoggedIn={setIsLoggedIn}
                    />

                        {!isReady
                            ? 'Is loading'
                            : products.map(product =>
                                <ProductCard {...product}/>
                        )}
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
                </Container>
            </Router>
        );
    }
}

const mapStateToProps = ({products}) =>({
   products: products.items,
   isReady: products.isReady
});

const mapDispatchToProps = dispatch => ({
    setProducts: products => dispatch(setProducts(products))
});


export default connect(mapStateToProps, mapDispatchToProps)(App);
