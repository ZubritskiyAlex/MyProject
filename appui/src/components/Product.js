import React from "react";

export default ({product}) => {
    return (
        <div className="card">
            <div className="card-body">
                <h5 className="card-title">{product.title}</h5>
            </div>
        </div>
 )
}
