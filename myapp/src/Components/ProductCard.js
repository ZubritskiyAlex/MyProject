import React from "react";

const ProductCard = (props) => {
    const {id, name, price} = props.product

  return(
      <div className="item">
          <img className="ui avatar image src = {product}" alt="product"/>
      <div className="content">
          <div className="header">{name}</div>
          <div>{price}</div>
          </div>
              <i
                  className="trash alternate outline icon"
                  style={{color:"red", marginTop: "7px"}}
              ></i>
          </div>
  );
};

export default ProductCard;