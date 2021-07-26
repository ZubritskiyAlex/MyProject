import React from "react";
import { Link } from "react-router-dom";
import shop from "../images/shop.png";

const ShopCard = (props) => {
  const { id, name, description, owner } = props.shop;
  return (
    <div className="item">
      <img className="ui avatar image" src={shop} alt="shop" />
      <div className="content">
        <Link
          to={{ pathname: `/shop/${id}`, state: { shop: props.shop } }}
        >
          <div className="header">{name}</div>
          <div>{description}</div>
          <div>{owner}</div>
        </Link>
      </div>
      <i
        className="trash alternate outline icon"
        style={{ color: "red", marginTop: "7px" }}
        onClick={() => props.clickHander(id)}
      ></i>
    </div>
  );
};

export default ShopCard;