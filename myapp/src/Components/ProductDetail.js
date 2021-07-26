import React from "react";
import {Link} from 'react-router-dom'
import product from "../images/productdetail.png"


const ProductDetail = (props) => {
    const {name, price, description, shop} = props.location.state.product;
  return(
      <div className="main">
      <div className="ui card centered">
      <div className="image">
          <img src={product} alt="product"/>
          </div>
          <div className="content">
              <div className="header">{name}</div>
              <div className="description">{price}</div>
              <div className="description">{description}</div>
              <div className="description">{shop}</div>
          </div>
          </div>
          <div className="center-div">
              <Link to ="/products">
              <button className="ui button blue center">Back to Product List </button>
              </Link>
          </div>
          </div>
  );
};

export default ProductDetail;