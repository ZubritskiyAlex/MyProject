import React from 'react'
import Header from "./Components/Header";
import ProductsContent from "./Components/ProductsContent";
import Footer from "./Components/Footer";



const App =() => {
    return(
        <div className='app-wrapper'>
            <Header/>
            <ProductsContent/>
            <Footer/>

        </div>

    )

}

export default App