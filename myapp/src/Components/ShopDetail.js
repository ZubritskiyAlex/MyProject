import React from "react";
import { Link } from "react-router-dom";
import shop from "../images/shop.png";

const ShopDetail = (props) => {
  const { name, description, owner } = props.location.state.shop;
  return (
    <div className="main">
      <div className="ui card centered">
        <div className="image">
          <img src={shop} alt="shop" />
        </div>
        <div className="content">
          <div className="header">{name}</div>
          <div className="description">{description}</div>
          <div className="description">{owner}</div>
        </div>
      </div>
      <div className="center-div">
        <Link to="/">
          <button className="ui button blue center">
            Back to Shop List
          </button>
        </Link>
      </div>
    </div>
  );
};

export default ShopDetail;