import React from "react";
import Product from "./Product";

export default ({products}) => {
    if (!products.length) {
        return <button className="btn btn-primary">Load products</button>
    }
    return products.map(product => <Product product={product} key={product}/>)
}