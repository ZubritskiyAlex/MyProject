import React from "react";
import {Link} from 'react-router-dom'
import product from "../images/product.png"

const ProductCard = (props) => {
    const {id, name, price, description, shop} = props.product;

  return(
      <div className="item">
      <img className="ui avatar image" src={product} alt="product"/>
      <div className="content">
          <Link to ={{pathname:`/product/${id}`, state:{product:props.product}}}>
          <div className="header">{name}</div>
          <div>{price}</div>
          <div>{description}</div>
          <div>{shop}</div>
          </Link>
          </div>
              <i
                  className="trash alternate outline icon"
                  style={{color:"red", marginTop: "7px", marginLeft: "10px"}}
                  onClick={() => props.clickHandler(id)}
              ></i>
              <Link to={{ pathname:`/edit`, state: {product:props.product}}}>
                 <i
                  className="edit alternate outline icon"
                  style={{color:"blue", marginTop: "7px"}}
                  onClick={() => props.clickHandler(id)}
              ></i>
              </Link>
          </div>
  );
};

export default ProductCard;