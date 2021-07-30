import React from "react";

export const Products = ({products}) => {
    return(
        <ul className="list-group">
            {products.map(
                product => (
                <li
                    className="list-group-item note"
                    key={product.id}
                >

                <div>
                    <strong>{product.title}</strong>
                    <small>{new Date().toLocaleTimeString()}</small>
                </div>
                <button type= "button"
                        className="btn btn-outline-danger btn-sm">
                    &times;
                    Hide the product</button>
                 </li>
                ))}
        </ul>
    )
}