import React, {useState} from 'react'
import Header from "./Components/Header";
import ProductsContent from "./Components/ProductsContent";
import Footer from "./Components/Footer";
import ProductList from "./Components/ProductList";
import CreateProduct from "./Components/CreateProduct";


function App() {
    const [products, setProducts] = useState([])
    return(
        <div className='ui container'>
            <Header/>
            <ProductsContent/>
            <Footer/>
            <CreateProduct/>
            <ProductList products={products}/>
        </div>
    );
}
export default App
