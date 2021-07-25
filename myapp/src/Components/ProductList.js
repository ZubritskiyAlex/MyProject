import React from "react";
import ProductCard from "./ProductCard";

const ProductList = (props) => {
    console.log(props);

    const renderProductList = props.products.map((product)=> {
        return <ProductCard product = {product}></ProductCard>;

    });

    return(
        <div className="ui celled list">
            {renderProductList}
        </div>
    );
};


export default ProductList;