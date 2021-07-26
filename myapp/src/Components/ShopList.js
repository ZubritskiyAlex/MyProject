import React from "react";
import { Link } from "react-router-dom";
import ShopCard from "./ShopCard";

const ShopList = (props) => {
  console.log(props);

  const deleteShopHandler = (id) => {
    props.getShopId(id);
  };

  const renderContactList = props.shops.map((shop) => {
    return (
      <ShopCard
        Shop={shop}
        clickHander={deleteShopHandler}
        key={shop.id}
      />
    );
  });
  return (
    <div className="main">
      <h2>
        Shop List
        <Link to="/add">
          <button className="ui button blue right">Create Shop!</button>
        </Link>
      </h2>
      <div className="ui celled list">{renderShopList}</div>
    </div>
  );
};

export default ShopList;